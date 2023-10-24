import abc
import time
from abc import abstractmethod
from typing import List


class SortingStrategy(metaclass=abc.ABCMeta):

    @abstractmethod
    def perform_sorting(self, data: List) -> List:
        pass


class BubbleSortStrategy(SortingStrategy):

    def perform_sorting(self, data: List) -> List:
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]
        return data


class MergeSortStrategy(SortingStrategy):

    def perform_sorting(self, data: List) -> List:
        return sorted(data)


class NumberList:

    def __init__(self, sorting_strategy: SortingStrategy):
        self._sorting_strategy = sorting_strategy

    @property
    def sorting_strategy(self):
        return self._sorting_strategy

    @sorting_strategy.setter
    def sorting_strategy(self, sorting_strategy: SortingStrategy):
        self._sorting_strategy = sorting_strategy

    def perform_sorting(self, data):
        print("Data before sorting", data)
        data = self._sorting_strategy.perform_sorting(data)
        print("Data after sorting", data)


if __name__ == "__main__":
    number_list = NumberList(BubbleSortStrategy())
    t = time.time_ns()
    number_list.perform_sorting(
        [5, 7, 43, 36, 23, 54, 4, 21, 43, 6, 2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 63324, 343456, 34, 34, 4, 364, 34, 346,
         346, 346, 346, 87])
    print(time.time_ns() - t)

    number_list.sorting_strategy = MergeSortStrategy()
    t = time.time_ns()
    number_list.perform_sorting(
        [5, 7, 43, 36, 23, 54, 4, 21, 43, 6, 2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 63324, 343456, 34, 34, 4, 364, 34, 346,
         346, 346, 346, 87])
    print(time.time_ns() - t)
