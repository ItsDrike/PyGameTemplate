from contextlib import suppress

from src.game import Game
from src.util.log import get_logger

log = get_logger(__name__)


if __name__ == "__main__":
    game = Game()

    log.info("Starting game")

    with suppress(KeyboardInterrupt):
        game.run_continually()

    log.info("Game Stopped")
