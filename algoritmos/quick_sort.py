from .base import AlgoritmoBase
from typing import List
import copy


class QuickSort(AlgoritmoBase):
    @AlgoritmoBase.timer_decorator
    def sort(self, array: List[int]) -> List[int]:
        """QuickSort"""
        self.input_array = array
        self.iterations = 0
        self.output_array = copy.deepcopy(self.input_array)

        if len(self.output_array) <= 1:
            return self.output_array

        self._quicksort(0, len(self.output_array) - 1)
        return self.output_array

    def _quicksort(self, low: int, high: int) -> None:
        if low < high:
            p = self._partition(low, high)
            self._quicksort(low, p - 1)
            self._quicksort(p + 1, high)

    def _partition(self, low: int, high: int) -> int:
        pivot = self.output_array[high]
        i = low - 1
        for j in range(low, high):
            self.iterations += 1
            if self.output_array[j] <= pivot:
                i += 1
                if i != j:
                    self.output_array[i], self.output_array[j] = (
                        self.output_array[j],
                        self.output_array[i],
                    )
        i += 1
        self.output_array[i], self.output_array[high] = (
            self.output_array[high],
            self.output_array[i],
        )
        return i
