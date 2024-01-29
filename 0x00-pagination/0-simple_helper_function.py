#!/usr/bin/env python3
"""
Simple helper function
"""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple:
    """ calculte start and end indices"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
