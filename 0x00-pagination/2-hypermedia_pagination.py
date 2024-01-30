#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ calculte start and end indices"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        requested dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()
        try:
            (start_index, end_index) = index_range(page, page_size)
            end_index = min(end_index, len(dataset))
            return dataset[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        to navigate through pages of data
        """
        dataset = self.dataset()
        lastpage = math.ceil(len(dataset) / page_size)

        hypermedia = {
            'page_size': len(dataset),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < lastpage else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': lastpage,
        }
        return hypermedia
