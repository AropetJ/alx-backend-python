#!/usr/bin/env python3
'''5-sum_list.py
'''
from typing import List


def sum_list(input_list: List) -> float:
    sum = 0
    for i in input_list:
        sum += i
    return float(sum)
