from pygame.event import EventType  # type: ignore (see: https://github.com/pygame/pygame/issues/2867)

from src.util.base_game import BaseGame
from src.util.color import Color


class Game(BaseGame):
    """Game class handling all game-related logic."""

    def handle_user_event(self, event: EventType) -> None:
        """Handle pygame events (f.e.: click, keydown)."""
        pass

    def redraw_screen(self) -> None:
        """
        Redraw everything on the screen.

        Usually this function runs draw functions on `self.surface`.

        Note: You shouldn't update the screen here (with `pygame.display.update()`) here
        because it already after this function is called from `self.start` method and
        since you're not expected to add some heavy time-taking logic here (that
        belongs in `self.tick`), there is generally no need to update the screen from here.
        """
        self.surface.fill(Color.GREY)

    def cleanup(self) -> None:
        """
        This is the function which will be ran last, as the main loop ends.

        Usually, `pygame.quit()` is executed immediately after this function ends,
        in which case this function can usually be left alone, however if the game
        is running continually (resetting each time self.running was set to False,
        until self.ended isn't True) there may be a need to perform some setup-like
        logic. Note that if a game is running continually, setup will run each time,
        so you don't need to copy over the same logic here.
        """
        pass

    def setup(self) -> None:
        """
        This is the function which will be ran initially, as static game setup.

        This function serves as a way to handle any long (or short) operations such as
        class initializations or variable definitions that are expected to occur before
        the main loop is started.

        Note that if a game is running continually (resetting each time self.running is False,
        until self.ended isn't True), the setup will be repeated across all of these runs,
        if setup contains some game-wide logic that shouldn't be recomputed after this reset,
        override the `continuous_setup` instead.
        """
        pass

    def continuous_setup(self) -> None:
        """
        This function is similar to `setup`, but it only runs once before the continuous loop starts.

        Just like setup only runs once before the game loop starts, this function only runs once before
        the continuous loop starts. This means that this function won't hang the game because it may have
        some complex time-intensive initialization tasks between each game reset.

        Note: This function won't be ran at all if the game isn't started with `run_continually`.
        """
        pass

    def tick(self) -> None:
        """
        This is the function which will be ran continually, every tick of the game.

        All heavy game logic is expected to go here, however you shouldn't draw anything
        to the screen from here, instead you should override the `redraw_screen` function,
        which is called before each tick.
        """
        pass
