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
        """Приводит значение к LogLevel или сообщает о некорректном уровне."""
        try:
            return cls(level)
        except ValueError:
            allowed = ", ".join(member.value for member in cls)
            raise ValueError(
                f"Unknown log level: {level!r}. Allowed levels: {allowed}"
            ) from None
