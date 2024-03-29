#!/usr/bin/env python3
"""
0x01. Python - Async
"""
wait = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """an async routine that spawn wait_random n times with the
    specified max_delay."""
    delays = []
    for _ in range(n):
        delays.append(await wait(max_delay))
    return delays
