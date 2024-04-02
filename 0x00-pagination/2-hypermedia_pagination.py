#!/usr/bin/env python3
"""
Hypermedia pagination.
"""
import csv
from typing import Tuple, List, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    end_index = page * page_size
    start_index = end_index - page_size
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
        Get the page as per the given arguments.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        content = dataset[start_index: end_index]
        return content

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Returns a dictionary containing the page's details and data.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        prev_page = page - 1
        total_pages = len(dataset) // page_size
        next_page = page + 1
        if len(data) == 0:
            page_size = 0
            next_page = None
        elif page * page_size >= len(dataset):  # Last page
            next_page = None
        elif page == 1:
            prev_page = None
        detail = {"page_size": page_size,
                  "page": page,
                  "data": data,
                  "next_page": next_page,
                  "prev_page": prev_page,
                  "total_pages": total_pages
                  }
        return detail
