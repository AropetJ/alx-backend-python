#!/usr/bin/env python3
'''8-make_multiplier.py
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that doubles a value

    Args:
        multiplier (float): The value to be doubled

    Returns:
        Callable[[float], float]: Function returned
    """
    return lambda z: z * multiplier
