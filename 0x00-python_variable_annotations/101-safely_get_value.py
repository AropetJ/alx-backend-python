#!/usr/bin/env python3
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Returns:
        Union[Any, T]: The value associated with the key, or the
        default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
