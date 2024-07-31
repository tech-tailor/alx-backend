#!/usr/bin/env python3
"""
0-simple_helper_function.py
The script returns a tuple of current and last indexes.
"""
from typing import Tuple
import csv
import math
from typing import List


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
        """The function that return cobntent of the page"""
        assert isinstance(page, int) and page > 0, "page must be greatern 0"
        assert isinstance(
            page_size, int) and page_size > 0, "page size must be greatern 0"

        datasetList = self.dataset()
        index = index_range(page, page_size)

        if 0 <= index[1] > len(datasetList) or index[0] > len(datasetList):
            return []
        result = [datasetList[i] for i in range(index[0], index[1])]
        return result


def index_range(page: int, page_size: int) -> Tuple:
    """
    The function returns a tuple of two which
    contains start and end indexes.
    """
    first_index = 1 * (page * page_size) - page_size
    last_index = first_index + page_size

    result = (first_index, last_index)
    return result
