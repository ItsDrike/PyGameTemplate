from src.util.typing import NumericType


def number_remap(
    number: NumericType,
    old_min: NumericType,
    old_max: NumericType,
    new_min: NumericType,
    new_max: NumericType,
) -> float:
    """
    Remap a given `number` ranging between given values to range between different values.

    For example, remapping a number ranging between 0 and 10 to new range of 0 and 100
    would result in following:
        >>> number_remap(1, 0, 10, 0, 100)
        10
        >>> number_remap(2, 0, 10, 0, 100)
        20
        >>> number_remap(10, 0, 10, 0, 100)
        100
    """
    if number > old_max or number < old_min:
        raise ValueError(f"Specified number: {number} is not within specified old range: <{old_min}, {old_max}>")

    return ((number - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
