#!/usr/bin/env python3
'''102-type_checking.py'''
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on an array by repeating each element a certain number of times.

    Args:
        lst (Tuple[int, ...]): The input array to be zoomed in.
        factor (int, optional): The number of times each element should be
        repeated. Defaults to 2.

    Returns:
        List[int]: The zoomed-in array.

    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
