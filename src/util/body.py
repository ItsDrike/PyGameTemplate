from abc import ABC, abstractmethod

import pygame

from src.config import Window
from src.util.descriptor import Coordinate
from src.util.typing import NumericType


class Body(ABC):
    """
    This is an abstract default class for an interactive body in pygame.

    This class is expected to be subclassed by a specific type of body
    which will include the needed specific functionality.
    """

    x = Coordinate(window_border=Window.width)
    y = Coordinate(window_border=Window.height)

    def __init__(self, x: NumericType, y: NumericType, width: NumericType, height: NumericType):
        self.x = x
        self.y = y
        self.width = float(width)
        self.height = float(height)

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        """Draw the Body object at a pygame surface."""
        raise NotImplementedError("`draw` is an abstract method, it must be implemented in the child class first.")

    @property
    def hitbox(self) -> pygame.Rect:
        """Get the rect hitbox of this body."""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides(self, other: "Body") -> bool:
        """Check if 2 bodies in collision with each other."""
        return all([
            self.hitbox.left < other.hitbox.right and self.hitbox.right > other.hitbox.left,  # X axis collision
            self.hitbox.top < other.hitbox.bottom and self.hitbox.bottom > other.hitbox.top,  # Y axis collision
        ])


class ControlledBody(Body):
    """
    This is an abstract default class for an interactive controlled body in pygame.

    This class is expected to be subclassed by a specific type of body
    which will include the needed specific functionality.
    """

    REQUIRED_MOVE_KEYS = ("left", "right", "up", "down")

    def __init__(
        self,
        x: NumericType,
        y: NumericType,
        width: NumericType,
        height: NumericType,
        velocity: NumericType,
        move_keys: dict[str, int]
    ):
        super().__init__(x, y, width, height)
        self.velocity = velocity
        self.move_keys = move_keys

    def move(self) -> None:
        """
        Move the object based on user's input accordingly to `self.move_keys`.

        If the user goes out of screen bounds ValueError will be raised,
        describing the out of bounds error and the coordinates will not be changed.

        You will most likely want to override this class to suppress this exception.
        """
        keys_pressed = pygame.key.get_pressed()

        for movement, key in self.move_keys.items():
            if keys_pressed[key]:
                if movement == "left":
                    self.x -= self.velocity
                elif movement == "right":
                    self.x += self.velocity
                elif movement == "up":
                    self.y -= self.velocity
                elif movement == "down":
                    self.y += self.velocity

    @property
    def move_keys(self) -> dict[str, int]:
        """Return the move_keys dictionary."""
        return self._move_keys

    @move_keys.setter
    def move_keys(self, value: dict[str, int]) -> None:
        """Ensure that move_keys dictionary contains all needed move_keys."""
        if not isinstance(value, dict):
            raise TypeError(f"move_keys must be a dict, got {value.__class__.__qualname__}")

        # Ensure we have all required keys
        for required_key in self.REQUIRED_MOVE_KEYS:
            if required_key not in value:
                raise ValueError(
                    f"move_keys must have `{self.REQUIRED_MOVE_KEYS}` defined, but {required_key} not found"
                )
            if not isinstance(value[required_key], int):  # Pygame characters are defined as integers
                obtained_type = value[required_key].__class__.__qualname__
                raise ValueError(f"move_keys[{required_key}] parameter must be a pygame key, got {obtained_type}")

        self._move_keys = value
