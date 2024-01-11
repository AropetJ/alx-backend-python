#!/usr/bin/env python3
'''9-element_length.py
'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in the given list.

    Args:
        lst (Iterable[Sequence]): The list of elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing each element
        and its length.
    """
    return [(i, len(i)) for i in lst]
