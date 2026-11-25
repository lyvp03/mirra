import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import split_design as sd


def names(pieces):
    return [p.filename for p in pieces]


def test_hash_inside_code_block_is_not_heading():
    text = "# Doc\n\n## 1. A\n\n### 1.1 B\n\n```python\n# not a heading\n## nor this\n```\n\ntail\n"
    pieces, _ = sd.split_file("01-X.md", text.split("\n")[:-1])
    assert names(pieces) == ["_overview.md", "1-a.md", "1-1-b.md"]
    b = pieces[-1]
    assert "# not a heading" in "\n".join(b.body) and "## nor this" in "\n".join(b.body)


def test_uc_heading_names_and_sub_uc_merged():
    lines = [
        "# T",
        "## 3. Spec",
        "### UC08 – Pay",
        "body",
        "#### UC08.1 – Sub",
        "sub body",
        "### 4.1 UC04 Quản lý hồ sơ",
        "x",
        "### 4.8 UC24, UC25 Quản lý",
        "y",
    ]
    pieces, _ = sd.split_file("01-UC.md", lines)
    assert names(pieces) == [
        "_overview.md",
        "3-spec.md",
        "UC08.md",
        "UC04.md",
        "UC24.md",
    ]
    uc08 = next(p for p in pieces if p.filename == "UC08.md")
    assert "UC08.1" in "\n".join(uc08.body)  # sub-UC stays in the same file
    assert sd.extract_ucs("UC08.1 và UC12–UC14") == {"UC08", "UC12", "UC13", "UC14"}


def test_duplicate_names_get_suffix():
    lines = ["# T", "## 1. A", "### Control", "x", "### Control", "y"]
    pieces, _ = sd.split_file("03-X.md", lines)
    assert names(pieces)[-2:] == ["control.md", "control-2.md"]


def test_database_table_names():
    lines = [
        "# T",
        "## 4. Từ điển",
        "### 4.2 auth\\_tokens — refresh token (UC01)",
        "x",
    ]
    pieces, _ = sd.split_file("04-DATABASE.md", lines)
    assert "auth-tokens.md" in names(pieces)


def test_table_never_cut_when_splitting_large_section():
    table = ["| a | b |", "| --- | --- |"] + [f"| {i} | x |" for i in range(40)]
    lines = ["# T", "## 1. Big", "intro"]
    for k in range(4):
        lines += [f"### 1.{k} Sec", ""] + ["text"] * 30 + [""] + table + [""]
        lines += [f"#### 1.{k}.1 Sub", ""] + ["more"] * 40 + [""] + table + [""]
    lines += ["### 1.9 Huge", ""]
    lines += [
        f"#### 1.9.{k} Part\n" + "\n".join(["w"] * 60 + [""] + table) for k in range(6)
    ]
    lines = "\n".join(lines).split("\n")
    pieces, _ = sd.split_file("02-X.md", lines)
    assert sum(len(p.body) for p in pieces) == len(lines)
    total_rows = sum(1 for l in lines if l.startswith("|"))
    assert sum(1 for p in pieces for l in p.body if l.startswith("|")) == total_rows
    for p in pieces:
        rows = [i for i, l in enumerate(p.body) if l.startswith("|")]
        # every table must remain intact as 42 consecutive lines
        runs, run = [], 0
        for i, r in enumerate(rows):
            run = run + 1 if i and r == rows[i - 1] + 1 else 1
            if i + 1 == len(rows) or rows[i + 1] != r + 1:
                runs.append(run)
        assert all(n == len(table) for n in runs), (p.filename, runs)
    # the section longer than 300 lines was split further
    assert any(p.filename.startswith("1-9-") for p in pieces)


def test_unsplittable_long_section_is_reported():
    lines = ["# T", "## 1. A", "### 1.1 Long"] + ["x"] * 320
    pieces, warns = sd.split_file("05-X.md", lines)
    assert len(pieces) == 3 and warns and "1.1 Long" in warns[0]


def _make_src(tmp: Path) -> Path:
    src = tmp / "src"
    src.mkdir()
    (src / "01-UC.md").write_text(
        "# UC\n\n```mermaid\nflowchart LR\n  U08([UC08 Thanh toán VietQR])\n```\n\n"
        "## 3. Spec\n\n### UC08 – Thanh toán\n\nNội dung. UC08.1 con.\n\n"
        "### UC09 – Theo dõi\n\nGiống UC08.\n",
        encoding="utf-8",
    )
    (src / "02-BCE.md").write_text(
        "# B2\n\n## 2. N\n\n### UC08 – Pay\n\n| a | b |\n|---|---|\n| 1 | 2 |\n",
        encoding="utf-8",
    )
    (src / "04-DATABASE.md").write_text(
        "# B4\n\n## 4. D\n\n### 4.1 payments — thanh toán (UC07, UC08.1)\n\nBảng.\n",
        encoding="utf-8",
    )
    (src / "notes.txt").write_text("ignore", encoding="utf-8")
    return src


def snapshot(out: Path) -> dict[str, str]:
    return {
        p.relative_to(out).as_posix(): p.read_text(encoding="utf-8")
        for p in sorted(out.rglob("*"))
        if p.is_file()
    }


def test_idempotent_and_only_touches_nn_dirs(tmp_path):
    src = _make_src(tmp_path)
    out = tmp_path / "out"
    (out / "99-stale").mkdir(parents=True)
    (out / "99-stale" / "old.md").write_text("old", encoding="utf-8")
    (out / "keep.txt").write_text("keep", encoding="utf-8")
    sd.run(src, out)
    first = snapshot(out)
    sd.run(src, out)
    second = snapshot(out)
    assert first == second
    assert "99-stale/old.md" not in first
    assert first["keep.txt"] == "keep"
    assert "01-uc/UC08.md" in first and "04-database/payments.md" in first


def test_index_columns_and_sub_uc(tmp_path):
    src = _make_src(tmp_path)
    out = tmp_path / "out"
    sd.run(src, out)
    index = (out / "INDEX.md").read_text(encoding="utf-8")
    row = next(l for l in index.splitlines() if l.startswith("| UC08 |"))
    assert "Thanh toán VietQR" in row
    assert "01-uc/UC08.md" in row and "02-bce/UC08.md" in row
    assert "04-database/payments.md" in row  # UC08.1 counts toward UC08
    assert "Đọc INDEX trước" in index
