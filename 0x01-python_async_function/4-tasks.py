#!/usr/bin/env python3
'''4-tasks.py
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times and returns a sorted list of the wait
    times.
    Args:
    - n: The number of times to execute task_wait_random.
    - max_delay: The maximum delay for each task_wait_random call.
    Returns:
    - A sorted list of the wait times.
    """
    wait_times = await asyncio.gather(*[task_wait_random(max_delay)
                                        for _ in range(n)])
    return sorted(wait_times)
