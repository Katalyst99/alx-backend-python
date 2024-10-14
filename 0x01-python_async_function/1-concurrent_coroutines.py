#!/usr/bin/env python3
"""The module for executing multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine that takes in 2 int arguments,
    should return the list of all the delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        todo = asyncio.create_task(wait_random(max_delay))
        tasks.append(todo)

    wait_times = []
    for todo in asyncio.as_completed(tasks):
        wait = await todo
        wait_times.append(wait)
    return wait_times
