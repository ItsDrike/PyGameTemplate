from typing import Any, Generic, TypeVar, cast

from src.util.typing import NumericType

T = TypeVar("T")


class Descriptor(Generic[T]):
    """
    This is a base descriptor implementation.

    It doesn't really do much but it provides us with a basis for all other
    descriptors, which can then override these methods (most notably the
    setter method) in order to impose restrictions.
    """

    def __set_name__(self, owner_cls: type[T], name: str) -> None:
        """
        Get the name of the descriptor variable.

        This method was is used to automatically detect the variable name used
        for given descriptor. This provides us with a unique variable we can
        later use as a key for the class dictionary, in which we will be storing
        the held values by the descriptor. (See PEP 487 for more details.)

        It also stores the owner class, which isn't used in the default
        implementation here, but it might be useful to have in some classes
        which build upon this one.
        """
        self.name = name
        self.cls = owner_cls

    def __get__(self, instance: T, owner_cls: type[T]) -> Any:
        """
        Implement default getter.

        This method will be called upon accessing the value held by this descriptor.
        """
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance: T, value: Any) -> None:
        """
        Implement default setter.

        This method will be called upon setting the value value to this descriptor.
        It uses internal instance dictionary (`__dict__`) to store the given value with
        a key of the variable name used to define this descriptor.
        """
        # This will not override the descriptor itself, because it is stored
        #  in class dictionary, not in instance dict.
        instance.__dict__[self.name] = value

    def __delete__(self, instance: T) -> None:
        """
        Implement default deleter.

        This method is called on deletion of the descriptor held value.
        It acts as a cleanup and completely removes the held value from memory.
        """
        del instance.__dict__[self.name]


class Coordinate(Descriptor[T]):
    """
    Coordinate parameter descriptor.

    This imposes window border bound restrictions automatically.
    Window size is received with init using `window_border` keyword argument.
    The setter will raise an exception if user will try to set the parameter to a:
        * non-float value -> `TypeError`
        * value outside of allowed bounds -> `ValueError`
    """

    def __init__(self, *args, window_border: NumericType, **kwargs):
        self.window_border = window_border

    def __get__(self, instance: T, owner_cls: type[T]) -> float:
        """Implement Coordinate getter."""
        ret = super().__get__(instance, owner_cls)
        return cast(float, ret)  # This will be float, since it's imposed in setter

    def __set__(self, instance: T, value: NumericType) -> None:
        """
        Implemnet Coordinate setter.

        - If the value isn't int/float, raise `TypeError`
        - If the value is out of given bounds, raise `ValueError`
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} coordinate must be `int` or `float`, got {value.__class__.__qualname__}")

        if value > self.window_border or value < 0:
            raise ValueError(f"Out of bounds: {self.window_border} can't be outside of the window (0-{self.window_border}), got {value}")

        return super().__set__(instance, float(value))
