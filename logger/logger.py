from __future__ import annotations

from datetime import datetime

from .levels import LogLevel
from .strategies import OutputStrategy


class Logger:
    """
    Context шаблона Strategy.

    Форматирует сообщение и делегирует его вывод стратегии,
    полученной извне. О конкретных способах вывода ничего не знает.
    """

    def __init__(self, strategy: OutputStrategy) -> None:
        self.strategy = strategy

    def log(self, level: LogLevel | str, message: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted = f"{timestamp} [{LogLevel.parse(level).value}] {message}"
        self.strategy.write(formatted)
        return formatted
