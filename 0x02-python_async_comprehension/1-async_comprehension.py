#!/usr/bin/env python3
'''1-async_comprehension.py
'''

from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async function that returns a list of floats generated from an async
    generator.
    Returns:
        List[float]: A list of floats generated from the async generator.
    """
    return [f async for f in async_generator()]
