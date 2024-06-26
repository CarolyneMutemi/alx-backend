#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        The goal here is that if between two queries,
        certain rows are removed from the dataset,
        the user does not miss items from dataset when changing page.
        Returns a dictionary.
        """
        indexed_data = self.indexed_dataset()
        assert isinstance(index, int) and index < len(indexed_data)
        assert isinstance(page_size, int) and page_size > 0
        data = []
        idx = index
        track_page_size = 0
        while track_page_size < page_size:
            row = indexed_data.get(idx)
            if row:
                track_page_size += 1
                data.append(row)
            idx += 1
        next_index = idx
        if page_size > len(indexed_data):
            page_size = len(indexed_data)
        if next_index >= len(indexed_data):
            next_index = None
        detail = {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
        return detail
