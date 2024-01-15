#!/usr/bin/env python3
'''1-concurrent_coroutines.py
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times and returns a sorted list of the wait times.

    Args:
    - n: The number of times to execute wait_random.
    - max_delay: The maximum delay for each wait_random call.

    Returns:
    - A sorted list of the wait times.
    """
    wait_times = await asyncio.gather(*[wait_random(max_delay)
                                        for _ in range(n)])
    return sorted(wait_times)
