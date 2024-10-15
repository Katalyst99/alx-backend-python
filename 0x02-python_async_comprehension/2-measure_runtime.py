#!/usr/bin/env python3
"""The module for Run time for four parallel comprehensions"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that will execute async_comprehension,
    four times in parallel using asyncio.gather.
    """
    start = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
