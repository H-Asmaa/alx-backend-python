#!/usr/bin/env python3
"""
0x01. Python - Async
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that returns an asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
