from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class OutputStrategy(ABC):
    """Strategy: общий интерфейс способа вывода готового сообщения."""

    @abstractmethod
    def write(self, message: str) -> None:
        """Выводит уже отформатированное сообщение."""


class ConsoleOutput(OutputStrategy):
    """ConcreteStrategy: вывод сообщения в консоль."""

    def write(self, message: str) -> None:
        print(message)


class FileOutput(OutputStrategy):
    """ConcreteStrategy: дозапись сообщения в текстовый файл."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def write(self, message: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as stream:
            stream.write(self._prepare(message) + "\n")

    def _prepare(self, message: str) -> str:
        """Точка расширения для преобразования сообщения перед записью."""
        return message


class UpperFileOutput(FileOutput):
    """ConcreteStrategy: запись в файл с переводом сообщения в верхний регистр."""

    def _prepare(self, message: str) -> str:
        return message.upper()
