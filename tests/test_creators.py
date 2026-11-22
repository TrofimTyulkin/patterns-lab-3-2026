import pytest

from logger import (
    ConsoleLoggerCreator,
    ConsoleOutput,
    FileLoggerCreator,
    FileOutput,
    LoggerCreator,
    UpperFileLoggerCreator,
    UpperFileOutput,
)


@pytest.mark.parametrize(
    ("creator", "expected"),
    [
        (ConsoleLoggerCreator(), ConsoleOutput),
        (FileLoggerCreator("app.log"), FileOutput),
        (UpperFileLoggerCreator("app.log"), UpperFileOutput),
    ],
)
def test_creator_builds_logger_with_its_strategy(
    creator: LoggerCreator, expected: type
) -> None:
    assert type(creator.create_logger().strategy) is expected
