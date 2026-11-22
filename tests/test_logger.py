import re

import pytest

from logger import ConsoleOutput, Logger, LogLevel


def test_message_format(capsys: pytest.CaptureFixture[str]) -> None:
    result = Logger(ConsoleOutput()).log(LogLevel.INFO, "hello")

    assert re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[INFO\] hello", result)
    assert capsys.readouterr().out == result + "\n"


@pytest.mark.parametrize("level", ["DEBUG", "info", None])
def test_invalid_level_is_rejected(level: object) -> None:
    with pytest.raises(ValueError, match="Unknown log level"):
        Logger(ConsoleOutput()).log(level, "hello")  # type: ignore[arg-type]
