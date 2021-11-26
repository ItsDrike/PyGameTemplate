import random

import pygame


class MetaColor(type):
    """
    Automatically initialize tuple color definitions in class variables.

    Whenever a new color class is created, find all class variables of
    tuple type of 3-4 items and assume those represent RGB(A) colors.
    Then convert all of these class variables into instances of this color
    class.
    """

    def __new__(cls, name: str, bases: tuple[type], cls_dict: dict):
        """Convert all color tuples into instances."""
        cls_obj = super().__new__(cls, name, bases, cls_dict)

        for name, value in cls_dict.items():
            if isinstance(value, tuple) and len(value) in (3, 4):  # Is color tuple
                # Make given class hold it's own instance for the color
                # class variables set as size 3/4 tuples: rgb(a)
                setattr(cls_obj, name, cls_obj(value))

        return cls_obj


class Color(pygame.Color, metaclass=MetaColor):
    """This class holds some pre-defined colors and extends pygame.Color class."""

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREY = 125, 125, 125
    RED = 240, 20, 30
    GREEN = 30, 255, 20
    BLUE = 100, 0, 255
    YELLOW = 255, 255, 0

    @classmethod
    def random(cls, random_alpha: bool = False) -> "Color":
        """
        Create a random color.

        By default, this random color will not be transparent (alpha value of 255),
        if random transparency is also desired, use `random_alpha=True`.
        """
        return cls(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255) if random_alpha else 255
        )
