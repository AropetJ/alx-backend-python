#!/usr/bin/env python3
'''3-tasks.py
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task object that wraps the
    wait_random function.
    Args:
        max_delay (int): The maximum delay in seconds.
    Returns:
        asyncio.Task: An asyncio.Task object representing the
        execution of wait_random function.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
