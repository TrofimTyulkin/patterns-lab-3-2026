from __future__ import annotations

from collections.abc import Callable
from datetime import datetime

from .levels import LogLevel
from .strategies import OutputStrategy

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


class Logger:
    """
    Context шаблона Strategy.

    Форматирует сообщение и делегирует его вывод стратегии,
    полученной извне. О конкретных способах вывода ничего не знает.
    """

    def __init__(
        self,
        strategy: OutputStrategy,
        clock: Callable[[], datetime] = datetime.now,
    ) -> None:
        self._strategy = strategy
        self._clock = clock

    @property
    def strategy(self) -> OutputStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: OutputStrategy) -> None:
        self._strategy = strategy

    def format(self, level: LogLevel | str, message: str) -> str:
        parsed = LogLevel.parse(level)
        timestamp = self._clock().strftime(TIMESTAMP_FORMAT)
        return f"{timestamp} [{parsed.value}] {message}"

    def log(self, level: LogLevel | str, message: str) -> str:
        formatted = self.format(level, message)
        self._strategy.write(formatted)
        return formatted
