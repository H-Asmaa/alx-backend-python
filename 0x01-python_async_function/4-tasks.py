#!/usr/bin/env python3
"""
0x01. Python - Async
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """an async routine that spawn task_wait_random n times with the
    specified max_delay."""
    delays = []
    for _ in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
