#!/usr/bin/env python3
"""PreToolUse (Edit|Write): block edits to docs/design/ and .env files.

Written in Python because this machine has no jq.
"""

import json
import os
import sys
from pathlib import Path

MESSAGE = (
    "Vùng bảo vệ. Muốn đổi thiết kế thì đề xuất ADR trong docs/adr/ và hỏi người dùng."
)


def is_protected(file_path: str, project_dir: str) -> bool:
    p = Path(file_path)
    if not p.is_absolute():
        p = Path(project_dir) / p
    p = Path(os.path.normcase(os.path.normpath(p)))
    name = p.name
    if name == ".env" or (name.startswith(".env.") and not name.endswith(".example")):
        return True
    design = Path(
        os.path.normcase(os.path.normpath(Path(project_dir) / "docs" / "design"))
    )
    return p == design or design in p.parents


def main() -> int:
    try:
        # Read bytes and decode as UTF-8: on Windows stdin defaults to the locale encoding,
        # which corrupts non-ASCII characters (e.g. "Đ") in the path.
        data = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return 0
    file_path = (data.get("tool_input") or {}).get("file_path") or ""
    if not file_path:
        return 0
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    if is_protected(file_path, project_dir):
        sys.stderr.reconfigure(encoding="utf-8")
        print(MESSAGE, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
