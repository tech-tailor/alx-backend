#!/usr/bin/env python3
"""
0-simple_helper_function.py
The script returns a tuple of current and last indexes.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    The function returns a tuple of two which
    contains start and end indexes.
    """
    first_index = 1 * (page * page_size) - page_size
    last_index = first_index + page_size

    result = (first_index, last_index)
    return result
