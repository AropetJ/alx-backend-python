#!/usr/bin/env python3
'''7-to_kv.py'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Annotated funcion that returns the square of a vakue

    Args:
        k (str): A key
        v (Union[int, float]): Value of the key

    Returns:
        Tuple[str, float]: Return value with the square of value
    """
    return (k, float(v**2))
