from pathlib import Path

import pytest

from logger import ConsoleOutput, FileOutput, UpperFileOutput


def test_console_output(capsys: pytest.CaptureFixture[str]) -> None:
    ConsoleOutput().write("hello")

    assert capsys.readouterr().out == "hello\n"


def test_file_output_appends(tmp_path: Path) -> None:
    path = tmp_path / "logs" / "app.log"
    strategy = FileOutput(path)

    strategy.write("first")
    strategy.write("Second")

    assert path.read_text(encoding="utf-8") == "first\nSecond\n"


def test_upper_file_output(tmp_path: Path) -> None:
    path = tmp_path / "app.log"

    UpperFileOutput(path).write("[ERROR] Something happened")

    assert path.read_text(encoding="utf-8") == "[ERROR] SOMETHING HAPPENED\n"
