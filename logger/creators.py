from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from .logger import Logger
from .strategies import ConsoleOutput, FileOutput, OutputStrategy, UpperFileOutput


class LoggerCreator(ABC):
    """
    Creator шаблона Factory Method.

    Объявляет фабричный метод create_strategy() и содержит общую логику
    сборки журнала, не зная, какая именно стратегия будет создана.
    """

    @abstractmethod
    def create_strategy(self) -> OutputStrategy:
        """Фабричный метод: создаёт конкретную стратегию вывода."""

    def create_logger(self) -> Logger:
        return Logger(self.create_strategy())


class ConsoleLoggerCreator(LoggerCreator):
    """ConcreteCreator: создаёт стратегию вывода в консоль."""

    def create_strategy(self) -> OutputStrategy:
        return ConsoleOutput()


class FileLoggerCreator(LoggerCreator):
    """ConcreteCreator: создаёт стратегию записи в файл."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def create_strategy(self) -> OutputStrategy:
        return FileOutput(self.path)


class UpperFileLoggerCreator(FileLoggerCreator):
    """ConcreteCreator: создаёт стратегию записи в файл в верхнем регистре."""

    def create_strategy(self) -> OutputStrategy:
        return UpperFileOutput(self.path)
