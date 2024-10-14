#!/usr/bin/env python3
"""
The basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    
    Args:
        max_delay: integer
    Returns: delay
    """
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
