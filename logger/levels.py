from __future__ import annotations

from enum import Enum


class LogLevel(str, Enum):
    TRACE = "TRACE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"

    @classmethod
    def parse(cls, level: LogLevel | str) -> LogLevel:
        try:
            return cls(level)
        except ValueError:
            raise ValueError(f"Unknown log level: {level!r}") from None
