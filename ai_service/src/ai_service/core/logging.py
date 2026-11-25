"""Process-wide logging setup (plain text for now; OpenTelemetry comes later, B5 6-4)."""

from __future__ import annotations

import logging

FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def configure_logging(level: str = "INFO") -> None:
    # basicConfig is a no-op when handlers already exist (uvicorn, pytest), so it never fights them.
    logging.basicConfig(level=level.upper(), format=FORMAT)
    logging.getLogger("ai_service").setLevel(level.upper())
