#!/usr/bin/env python3
'''5-sum_list.py
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of list items

    Args:
        input_list (List): A list of floats

    Returns:
        float: Sum of the list items
    """
    sum = 0
    for i in input_list:
        sum += i
    return float(sum)
