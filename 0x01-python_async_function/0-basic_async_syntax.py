#!/usr/bin/env python3
"""The module for an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer argument,
    named wait_random that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    waits = random.uniform(0, max_delay)
    await asyncio.sleep(waits)
    return waits
