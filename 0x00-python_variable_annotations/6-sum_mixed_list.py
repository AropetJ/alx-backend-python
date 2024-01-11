#!/usr/bin/env python3
'''6-sum_mixed_list.py
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a mixed argument list

    Args:
        mxd_lst (List[int, float]): List of ints and floats to be added

    Returns:
        float: Returned sum as a float
    """
    return float(sum(mxd_lst))
