#!/usr/bin/env python3
'''2-measure_runtime.py
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of the wait_n function.
    Args:
        n (int): The number of times to call the wait_n function.
        max_delay (int): The maximum delay in seconds for each call to wait_n.
    Returns:
        float: The average runtime of the wait_n function in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
