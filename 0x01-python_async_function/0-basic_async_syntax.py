#!/usr/bin/env python3
"""
0x01. Python - Async
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """An asynchronous coroutine that waits for a random delay
    between 0 and max_delay."""
    await asyncio.sleep(max_delay)
    return random.random()
