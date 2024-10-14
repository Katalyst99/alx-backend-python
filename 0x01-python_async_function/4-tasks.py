#!/usr/bin/env python3
"""The module for executing multiple coroutines at the same time with async"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine that takes in 2 int arguments,
    should return the list of all the delays in ascending order.
    except task_wait_random is being called.
    """
    tasks = []
    for _ in range(n):
        todo = task_wait_random(max_delay)
        tasks.append(todo)

    wait_times = await asyncio.gather(*tasks)
    return wait_times
