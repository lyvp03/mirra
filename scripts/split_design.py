#!/usr/bin/env python3
"""Split the monolithic Mirra design docs into many small files plus INDEX.md.

Usage:  python scripts/split_design.py [--src ../mirra-export] [--out docs/design]

Splitting rules:
  * Split at level-2 and level-3 headings. A level-2 section with children becomes an
    intro file plus one file per child; a level-2 section without children is one file
    (e.g. 08, 09, the ERDs in 04).
  * A section longer than MAX_LINES that has child headings is split at the next level.
  * Only headings outside code blocks are split points, so a code block or table is never cut.
  * A heading starting with a UC code -> UCxx.md. In 04: the table name. Otherwise: a slug
    with the section number, translated to English via scripts/filename_map.py
    (all file names are English).
  * Each small file starts with a "Nguồn: ..." (source) line, followed by the verbatim content.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from filename_map import RENAME

MAX_LINES = 300
SOURCE_PREFIX = "Nguồn: "

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(\S.*?)[ \t]*$")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
UC_LEADING_RE = re.compile(r"^(?:\d+(?:\.\d+)*\.?\s+)?(UC\d{2})(?:\.\d+)?\b")
UC_RE = re.compile(r"\bUC(\d{2})(?:\.\d+)?\b")
UC_RANGE_RE = re.compile(r"\bUC(\d{2})(?:\.\d+)?\s*[–-]\s*UC(\d{2})(?:\.\d+)?\b")
TABLE_NAME_RE = re.compile(r"^\d+(?:\.\d+)*\.?\s+(.+?)\s+[—–]\s+")

# Output directory (by NN prefix) -> column in the INDEX use-case table
UC_COLUMNS = {
    "01": "01-uc",
    "02": "02-bce",
    "04": "04-db",
    "05": "05-api",
    "06": "06-class",
    "07": "07-ai",
    "09": "09-test",
}


# --------------------------------------------------------------------------- reading & parsing


def read_lines(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return lines


def parse_headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """Return [(line index, level, text)] for headings outside code blocks."""
    result = []
    fence: tuple[str, int] | None = None
    for i, line in enumerate(lines):
        m = FENCE_RE.match(line)
        if m:
            marker, rest = m.group(1), m.group(2)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1] and not rest.strip():
                fence = None
            continue
        if fence is not None:
            continue
        h = HEADING_RE.match(line)
        if h:
            result.append((i, len(h.group(1)), h.group(2)))
    return result


@dataclass
class Node:
    level: int
    text: str
    start: int
    end: int = 0
    parent: Node | None = None
    children: list[Node] = field(default_factory=list)

    def path(self) -> list[str]:
        out, n = [], self
        while n is not None and n.level > 0:
            out.append(n.text)
            n = n.parent
        return out[::-1]


def build_tree(lines: list[str]) -> Node:
    root = Node(0, "", 0, len(lines))
    stack = [root]
    for idx, level, text in parse_headings(lines):
        while stack[-1].level >= level:
            stack.pop().end = idx
        node = Node(level, text, idx, parent=stack[-1])
        stack[-1].children.append(node)
        stack.append(node)
    for n in stack[1:]:
        n.end = len(lines)
    return root


@dataclass
class Unit:
    kind: str  # overview | intro | leaf
    node: Node | None
    start: int
    end: int


def collect(
    node: Node,
    units: list[Unit],
    warns: list[str],
    total: int,
    is_first_h1: bool = False,
) -> None:
    first = node.children[0].start if node.children else node.end
    if node.level == 0:
        if not node.children:
            if total:
                units.append(Unit("overview", None, 0, total))
            return
        c0 = node.children[0]
        if c0.level > 1 and c0.start > 0:
            units.append(Unit("overview", None, 0, c0.start))
        for i, c in enumerate(node.children):
            collect(c, units, warns, total, is_first_h1=(i == 0))
        return
    if node.level == 1:
        start = 0 if is_first_h1 else node.start
        units.append(Unit("overview", node, start, first))
        for c in node.children:
            collect(c, units, warns, total)
        return
    size = node.end - node.start
    if node.children and (node.level == 2 or size > MAX_LINES):
        units.append(Unit("intro", node, node.start, first))
        for c in node.children:
            collect(c, units, warns, total)
    else:
        if size > MAX_LINES:
            warns.append(
                f"{'#' * node.level} {node.text} ({size} dòng): không có heading con để tách tiếp"
            )
        units.append(Unit("leaf", node, node.start, node.end))


# --------------------------------------------------------------------------- naming


def slug(text: str, limit: int = 80) -> str:
    t = text.replace("\\", "").replace("đ", "d").replace("Đ", "D")
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    if len(t) > limit:
        cut = t[:limit]
        t = cut.rsplit("-", 1)[0] if "-" in cut and t[limit] != "-" else cut
    return t or "section"


def dir_name(stem: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")


def base_name(heading: str, dirname: str) -> str:
    m = UC_LEADING_RE.match(heading.replace("\\", ""))
    if m:
        return m.group(1)
    if dirname.startswith("04"):
        t = TABLE_NAME_RE.match(heading)
        if t:
            return slug(t.group(1))
    return slug(heading)


class Namer:
    def __init__(self) -> None:
        self.used: dict[str, int] = {}

    def unique(self, base: str) -> str:
        key = base.lower()
        n = self.used.get(key, 0) + 1
        self.used[key] = n
        return base if n == 1 else f"{base}-{n}"


# --------------------------------------------------------------------------- splitting one file


@dataclass
class Piece:
    dirname: str
    filename: str  # includes .md
    lines: list[str]  # includes the leading "Nguồn:" (source) line
    body: list[str]  # verbatim content, without the source line

    @property
    def rel(self) -> str:
        return f"{self.dirname}/{self.filename}"


def split_file(
    src_name: str, lines: list[str], rename: dict[str, str] | None = None
) -> tuple[list[Piece], list[str]]:
    dirname = dir_name(Path(src_name).stem)
    root = build_tree(lines)
    units: list[Unit] = []
    warns: list[str] = []
    collect(root, units, warns, len(lines))
    namer = Namer()
    pieces = []
    covered = 0
    for u in units:
        if u.kind == "overview":
            base = "_overview"
            source = f"{SOURCE_PREFIX}{src_name}"
        else:
            base = base_name(u.node.text, dirname)
            if rename is not None:
                is_code = re.fullmatch(r"UC\d{2}", base) or (
                    dirname.startswith("04") and not base[0].isdigit()
                )
                if base in rename:
                    base = rename[base]
                elif not is_code:
                    warns.append(
                        f"chưa có tên tiếng Anh cho '{base}' (thêm vào scripts/filename_map.py)"
                    )
            source = f"{SOURCE_PREFIX}{src_name} > " + " > ".join(u.node.path())
        body = lines[u.start : u.end]
        covered += len(body)
        pieces.append(Piece(dirname, namer.unique(base) + ".md", [source] + body, body))
    assert covered == len(lines), (
        f"{src_name}: tách mất dòng ({covered} != {len(lines)})"
    )
    return pieces, [f"{src_name}: {w}" for w in warns]


# --------------------------------------------------------------------------- INDEX


def extract_ucs(text: str) -> set[str]:
    found = {f"UC{m.group(1)}" for m in UC_RE.finditer(text)}
    for m in UC_RANGE_RE.finditer(text):
        a, b = int(m.group(1)), int(m.group(2))
        if a <= b and b - a <= 15:
            found.update(f"UC{n:02d}" for n in range(a, b + 1))
    return found


def uc_names(lines: list[str]) -> dict[str, str]:
    names: dict[str, str] = {}
    text = "\n".join(lines)
    for m in re.finditer(r"\(\[(UC\d{2}) ([^\]]+?)\]\)", text):
        names.setdefault(m.group(1), m.group(2).strip())
    for line in lines:
        h = re.match(r"^#{1,6}\s+(UC\d{2})\s+[–-]\s+(.+?)(?:\s*\(.*)?$", line)
        if h:
            names.setdefault(h.group(1), h.group(2).strip())
            continue
        h = re.match(r"^#{1,6}\s+\d+\.\d+\s+(UC\d{2})\s+(.+?)\s*\(", line)
        if h:
            names.setdefault(h.group(1), h.group(2).strip())
    return names


def first_sentence(body: list[str]) -> str:
    for raw in body:
        s = raw.strip()
        if not s or s.startswith(("#", SOURCE_PREFIX)) or FENCE_RE.match(raw):
            continue
        if s.startswith("|"):
            if re.match(r"^\|?[\s:|-]+\|?$", s):
                continue
            s = " / ".join(c.strip() for c in s.strip("|").split("|"))
        s = re.sub(r"^(>|[-*+]|\d+\.)\s+", "", s)
        s = s.replace("**", "").replace("`", "")
        s = re.split(r"(?<=[.!?])\s+", s)[0]
        if len(s) > 120:
            s = s[:117].rstrip() + "…"
        return s.replace("|", "\\|")
    return ""


def uc_sort_key(code: str) -> int:
    return int(code[2:])


def build_index(
    pieces: list[Piece], sources: dict[str, list[str]]
) -> tuple[str, list[str]]:
    uc01 = next((v for k, v in sources.items() if k.startswith("01-")), [])
    names = uc_names(uc01)
    codes = set(names) | extract_ucs("\n".join(uc01))
    warns = [
        f"Không tìm thấy tên cho {c} trong 01-UC"
        for c in sorted(codes, key=uc_sort_key)
        if c not in names
    ]

    cols = list(UC_COLUMNS.values())
    table: dict[str, dict[str, list[str]]] = {
        c: {col: [] for col in cols} for c in codes
    }
    for p in pieces:
        col = UC_COLUMNS.get(p.dirname[:2])
        if not col:
            continue
        for code in extract_ucs("\n".join(p.body)) & codes:
            table[code][col].append(p.rel)

    def cell(code: str, paths: list[str]) -> str:
        paths = sorted(paths, key=lambda r: (Path(r).stem != code, r))
        return "<br>".join(paths)

    out = [
        "# INDEX thiết kế Mirra",
        "",
        "Sinh tự động bởi `scripts/split_design.py`. Đừng sửa tay.",
        "",
    ]
    out += ["## 1. Bảng UC", ""]
    out.append("| UC | Tên | " + " | ".join(cols) + " |")
    out.append("|" + "---|" * (len(cols) + 2))
    for code in sorted(codes, key=uc_sort_key):
        name = names.get(code, "").replace("|", "\\|")
        out.append(
            f"| {code} | {name} | "
            + " | ".join(cell(code, table[code][c]) for c in cols)
            + " |"
        )
    out += ["", "## 2. Bảng file", "", "| File | Dòng | Câu đầu |", "|---|---|---|"]
    for p in pieces:
        out.append(f"| {p.rel} | {len(p.lines)} | {first_sentence(p.body)} |")
    out += [
        "",
        "## 3. Cách dùng",
        "",
        "Đọc INDEX trước, chỉ mở file cần thiết, không đọc cả thư mục.",
        "",
    ]
    return "\n".join(out), warns


# --------------------------------------------------------------------------- main


def run(src: Path, out: Path) -> dict:
    files = sorted(p for p in src.glob("*.md") if p.is_file())
    if not files:
        raise SystemExit(f"Không có file .md nào trong {src}")
    pieces: list[Piece] = []
    warns: list[str] = []
    sources: dict[str, list[str]] = {}
    for f in files:
        lines = read_lines(f)
        sources[f.name] = lines
        ps, w = split_file(f.name, lines, RENAME)
        pieces += ps
        warns += w
    index, iw = build_index(pieces, sources)
    warns += iw

    out.mkdir(parents=True, exist_ok=True)
    for d in out.iterdir():
        if d.is_dir() and re.match(r"^\d{2}-", d.name):
            shutil.rmtree(d)
    for p in pieces:
        target = out / p.dirname / p.filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(p.lines) + "\n", encoding="utf-8", newline="\n")
    (out / "INDEX.md").write_text(index, encoding="utf-8", newline="\n")
    return {"pieces": pieces, "warnings": warns, "sources": sources}


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--src", type=Path, default=Path("../mirra-export"))
    ap.add_argument("--out", type=Path, default=Path("docs/design"))
    args = ap.parse_args(argv)
    res = run(args.src, args.out)
    counts: dict[str, int] = {}
    for p in res["pieces"]:
        counts[p.dirname] = counts.get(p.dirname, 0) + 1
    for d, n in counts.items():
        print(f"{d}: {n} file")
    print(f"Tổng: {len(res['pieces'])} file -> {args.out}")
    for w in res["warnings"]:
        print("CẢNH BÁO:", w)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
