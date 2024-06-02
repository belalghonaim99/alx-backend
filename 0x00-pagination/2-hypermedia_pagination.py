#!/usr/bin/env python3
"""Hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple of size two containing
    a start index and an end index"""

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self._data_set = None

    def dataset(self) -> List[List]:
        """Loads dataset from csv file and returns it."""
        if self._data_set is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data_set = [row for row in reader]
            self._data_set = data_set[1:]

        return self._data_set

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset."""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_data, end_da = index_range(page, page_size)
        data = self.dataset()
        if start_data > len(data):
            return []
        return data[start_data:end_da]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves information about a page.
        """
        data = self.get_page(page, page_size)
        starting, ending = index_range(page, page_size)
        total_pages = math.ceil(len(self._data_set) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if ending < len(self._data_set) else None,
            'prev_page': page - 1 if starting > 0 else None,
            'total_pages': total_pages
        }
