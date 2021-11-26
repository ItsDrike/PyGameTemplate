import os

DEBUG = "DEBUG" in os.environ and os.environ["DEBUG"].lower() != "false"
TRACE_LOGGERS = os.getenv("GAME_TRACE_LOGGERS", None)


class Window:
    """This class holds global configuration values for the game window."""

    tick_rate = 30
    height = 600
    width = 800
