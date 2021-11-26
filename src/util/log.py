import logging
import logging.handlers
import os
import sys
from pathlib import Path
from typing import Optional, TYPE_CHECKING, cast

import coloredlogs

import src.config

FORMAT_STRING = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

TRACE_LEVEL = 5


if TYPE_CHECKING:
    LoggerClass = logging.Logger
else:
    LoggerClass = logging.getLoggerClass()


class CustomLogger(LoggerClass):
    """Custom implementation of the `Logger` class with an added `trace` method."""

    def trace(self, msg: str, *args, **kwargs) -> None:
        """
        Log 'msg % args' with severity 'TRACE'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.
        logger.trace("Houston, we have an %s", "interesting problem", exc_info=1)
        """
        if self.isEnabledFor(TRACE_LEVEL):
            self.log(TRACE_LEVEL, msg, *args, **kwargs)


def get_logger(name: Optional[str] = None) -> CustomLogger:
    """Utility to make mypy recognize that logger is of type `CustomLogger`."""
    return cast(CustomLogger, logging.getLogger(name))


def setup_coloredlogs(format_string: str, root_log: logging.Logger) -> None:
    """Set up style of coloredlogs."""
    if "COLOREDLOGS_LEVEL_STYLES" not in os.environ:
        coloredlogs.DEFAULT_LEVEL_STYLES = {
            **coloredlogs.DEFAULT_LEVEL_STYLES,
            "trace": {"color": 246},
            "critical": {"background": "red"},
            "debug": coloredlogs.DEFAULT_LEVEL_STYLES["info"]
        }

    if "COLOREDLOGS_LOG_FORMAT" not in os.environ:
        coloredlogs.DEFAULT_LOG_FORMAT = format_string

    coloredlogs.install(level=TRACE_LEVEL, logger=root_log, stream=sys.stdout)


def _set_trace_loggers() -> None:
    """
    Set loggers to the trace level according to the value from the GAME_TRACE_LOGGERS env var.

    When the env var is a list of logger names delimited by a comma,
    each of the listed loggers will be set to the trace level.

    If this list is prefixed with a "!", all of the loggers except the listed ones will be set to the trace level.

    Otherwise if the env var begins with a "*",
    the root logger is set to the trace level and other contents are ignored.
    """
    if not src.config.TRACE_LOGGERS:
        return

    level_filter = src.config.TRACE_LOGGERS

    if level_filter.startswith("*"):
        # All loggers will be at trace level
        get_logger().setLevel(TRACE_LEVEL)
        level_filter = level_filter.removeprefix("*,")

    elif level_filter.startswith("!"):
        # All loggers except those specified will be at trace level
        get_logger().setLevel(TRACE_LEVEL)
        for logger_name in level_filter.strip("!,").split(","):
            get_logger(logger_name).setLevel(logging.DEBUG if src.config.DEBUG else logging.INFO)

    else:
        # Specified loggers will be at trace level
        for logger_name in level_filter.strip(",").split(","):
            get_logger(logger_name).setLevel(TRACE_LEVEL)


def setup() -> None:
    """Set up loggers."""
    # Configure global logging format
    log_format = logging.Formatter(FORMAT_STRING)

    # Add global TRACE level
    logging.TRACE = TRACE_LEVEL  # type: ignore
    logging.addLevelName(TRACE_LEVEL, "TRACE")
    logging.setLoggerClass(CustomLogger)

    # Configure the root logger
    root_log = get_logger()
    setup_coloredlogs(FORMAT_STRING, root_log)
    root_log.setLevel(logging.DEBUG if src.config.DEBUG else logging.INFO)

    # Configure file handler (if enabled)
    if src.config.FILE_LOG:
        log_file = Path("logs", "game.log")
        log_file.parent.mkdir(exist_ok=True)
        file_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=5242880, backupCount=7, encoding="utf8")
        file_handler.setFormatter(log_format)
        root_log.addHandler(file_handler)

    # Configure log-levels for other loggers
    logging.getLogger("PIL").setLevel(logging.INFO)

    # Set TRACE log level for defined loggers
    _set_trace_loggers()
