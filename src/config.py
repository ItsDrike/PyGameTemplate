import os


def get_env_bool(env_name: str) -> bool:
    """
    Get a boolean environment variable value.

    - If the env variable isn't defined, return `False`
    - If the env variable holds string representing false, return `False`
    - Otherwise return `True`
    """
    if env_name not in os.environ:
        return False

    value = os.environ[env_name].lower()
    return value not in {"false", "0", "no", "disable"}


DEBUG = get_env_bool("DEBUG")
FILE_LOG = get_env_bool("FILE_LOG")
TRACE_LOGGERS = os.getenv("GAME_TRACE_LOGGERS", None)


class Window:
    """This class holds global configuration values for the game window."""

    tick_rate = 30
    height = 600
    width = 800
