import math
from typing import Any, Generic, TypeVar

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


class TypedDescriptor(Descriptor[T]):
    """
    Decorator which only accepts values of given type(s).

    This class is expected to be subclassed and override the class variables
    `allowed_types`, holding the tuple of accepted types, for isinstance checks.
    """

    allowed_types = (object, )

    def check(self, value: Any) -> None:
        """Ensure given `value` meets the requirements."""
        if not isinstance(value, self.allowed_types):
            if len(self.allowed_types) == 1:
                types_msg = f"must be of type: `{self.allowed_types[0]}`"
            else:
                joined = ", ".join(f"`{typ}`" for typ in self.allowed_types)
                types_msg = f"type must be one of: {joined}"

            raise TypeError(f"{self.name} {types_msg}, got `{value.__class__.__qualname__}`")

    def __set__(self, instance: T, value: Any) -> None:
        """Only allow setting values which mach the expected types."""
        self.check(value)
        return super().__set__(instance, value)


class Numeric(TypedDescriptor[T]):
    """
    Any number (int/float).

    The setter will raise an exception if the user will try to set the parameter to a
    non-numeric value (TypeError).
    """

    allowed_types = (float, int)
    ValueType = NumericType


class NumericRange(Numeric[T]):
    """
    Any number within specified range.

    Range is received with init using `min` and `max` keyword arguments, both `min`
    and `max` are included in this range.

    The setter will raise an exception if user will try to set the parameter to a:
        * non-numeric value -> `TypeError`
        * value outside of allowed range -> `ValueError`
    """

    def __init__(self, *args, min: NumericType, max: NumericType, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.min = min
        self.max = max

    def check(self, value: Any) -> None:
        """Ensure given `value` meets the requirements."""
        super().check(value)
        if value < self.min or value > self.max:
            raise ValueError(f"Given value ({value}) is outside the allowed range <{self.min}-{self.max}>.")


class RadianAngle(NumericRange[T]):
    """
    Angle represented as a number in radians.

    If a number is outside of the allowed range, it is automatically
    adjusted (value % 2 * pi) to always represent a valid basic radian angle.

    The setter will raise an exception if user will try to set the parameter to
    a non-numeric value (TypeError).
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, min=0, max=(2 * math.pi), **kwargs)

    def __set__(self, instance: T, value: Any) -> None:
        """Automatically adjust value to fit within the base radian range."""
        # We don't adjust the number first because it may not even be of
        # numeric type, running the checks first ensures that it is numeric
        # and will fail with ValueError only if it's outside of specified range.
        try:
            self.check(value)
        except ValueError:
            value = value % 2 * math.pi
        return super().__set__(instance, value)


class Coordinate(NumericRange[T]):
    """
    Coordinate parameter descriptor.

    This imposes window border bound restrictions automatically.
    Window size is received with init using `window_border` keyword argument.

    The setter will raise an exception if user will try to set the parameter to a:
        * non-numeric value -> `TypeError`
        * value outside of allowed bounds -> `ValueError`
    """

    def __init__(self, *args, window_border: NumericType, **kwargs):
        self.window_border = window_border
        super().__init__(*args, min=0, max=self.window_border, **kwargs)
