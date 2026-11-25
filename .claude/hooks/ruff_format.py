#!/usr/bin/env python3
"""PostToolUse (Edit|Write): for .py files, run ruff format then ruff check --fix on that file only."""

import json
import shutil
import subprocess
import sys


def main() -> int:
    try:
        # Read bytes and decode as UTF-8: on Windows stdin defaults to the locale encoding,
        # which corrupts non-ASCII characters (e.g. "Đ") in the path.
        data = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return 0
    file_path = (data.get("tool_input") or {}).get("file_path") or ""
    if not file_path.endswith(".py"):
        return 0
    ruff = ["ruff"] if shutil.which("ruff") else ["uvx", "ruff"]
    if not shutil.which(ruff[0]):
        print("Bỏ qua ruff: không tìm thấy ruff hoặc uvx.", file=sys.stderr)
        return 0
    for args in (["format", file_path], ["check", "--fix", file_path]):
        r = subprocess.run(
            ruff + args, check=False, capture_output=True, text=True, encoding="utf-8"
        )
        if r.returncode != 0 and args[0] == "check":
            # Report remaining lint errors to Claude (exit 2 feeds stderr back into context).
            # The edit has already been applied, so nothing is blocked.
            print((r.stdout + r.stderr).strip(), file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
