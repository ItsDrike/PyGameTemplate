from abc import abstractmethod

import pygame
from pygame.event import EventType  # type: ignore (see: https://github.com/pygame/pygame/issues/2867)

from src.util.log import get_logger

log = get_logger(__name__)


class BaseGame:
    """
    Default implementation of a game class.

    You are expected to subclass this class and add the functionality needed
    for your specific game. This class only contains some default functions
    and parameters which are useful for every game.
    """

    def __init__(self, width: int, height: int, fps: int) -> None:
        self.size = self.width, self.height = width, height

        self.surface = pygame.display.set_mode(self.size)
        self.fps_clock = pygame.time.Clock()
        self.tick_rate = fps

        self.running = True
        self.ended = False

    @property
    def running(self) -> bool:
        """The game can only be running if it hasn't already been ended."""
        if self.ended and self._running is True:
            log.trace("Running is true but the game was already marked as ended, forcing False.")
            return False
        return self._running

    @running.setter
    def running(self, value: bool) -> None:
        """Set the value of running property."""
        self._running = value

    def run_continually(self) -> None:
        """Keep resetting the game until `self.ended` is `True`."""
        log.trace("Starting pygame")
        pygame.init()

        # Continuous loop
        log.debug("Starting continuous game")
        while self.ended is False:
            self.running = True
            self.start(manage_pygame=False)
            if self.ended is False:  # Only print this if `self.ended` wasn't already set to `False`
                log.debug("Restarting game loop (continual run)")

        log.debug("Stopping continuous game")
        log.trace("Stopping pygame")
        pygame.quit()

    def start(self, manage_pygame: bool = True) -> None:
        """
        Run the game once.

        Set `manage_pygame` to `False` if you want to manage pygame manually
        (handles `pygame.init()` and `pygame.quit()` methods). This could be useful
        if you want to have multiple games managed by different game classes or
        to continually run a game which could be useful for full game restarts
        without having to restart the whole program.
        """
        # Initialization
        if manage_pygame:
            log.trace("Starting pygame")
            pygame.init()
        log.debug("Starting the game loop")
        self.setup()

        # Continual game loop
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._handle_quit_event()

                self.handle_user_event(event)

            # _handle_quit_event could've already stopped the game,
            # we don't want to run the tick logic here since it could
            # take too long when the game is already expected to stop.
            if not self.running:
                break

            self.redraw_screen()
            pygame.display.update()

            self.tick()
            self.fps_clock.tick(self.tick_rate)

        # Final cleanup
        self.cleanup()
        log.debug("Stopping the game loop")
        if manage_pygame:
            log.trace("Stopping pygame")
            pygame.quit()

    def _handle_quit_event(self) -> None:
        """
        Handle pygame quitting event.

        This is implemented outside of the `handle_user_event`, because the
        user may forget to add this functionality leading to issues with not
        being able to properly terminate the program.

        In case quitting should do something else, this can be overridden, but
        it usually isn't needed.
        """
        self.running = False
        self.ended = True

    @abstractmethod
    def handle_user_event(self, event: EventType) -> None:
        """Handle pygame events (f.e.: click, keydown)."""
        pass

    @abstractmethod
    def redraw_screen(self) -> None:
        """
        Redraw everything on the screen.

        Usually this function runs draw functions on `self.surface`.

        Note: You shouldn't update the screen here (with `pygame.display.update()`) here
        because it already after this function is called from `self.start` method and
        since you're not expected to add some heavy time-taking logic here (that
        belongs in `self.tick`), there is generally no need to update the screen from here.
        """
        pass

    @abstractmethod
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

    @abstractmethod
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

    @abstractmethod
    def continuous_setup(self) -> None:
        """
        This function is similar to `setup`, but it only runs once before the continuous loop starts.

        Just like setup only runs once before the game loop starts, this function only runs once before
        the continuous loop starts. This means that this function won't hang the game because it may have
        some complex time-intensive initialization tasks between each game reset.

        Note: This function won't be ran at all if the game isn't started with `run_continually`.
        """
        pass

    @abstractmethod
    def tick(self) -> None:
        """
        This is the function which will be ran continually, every tick of the game.

        All heavy game logic is expected to go here, however you shouldn't draw anything
        to the screen from here, instead you should override the `redraw_screen` function,
        which is called before each tick.
        """
        pass
