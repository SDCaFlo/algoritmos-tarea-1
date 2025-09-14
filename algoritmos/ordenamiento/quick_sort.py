from .base import AlgoritmoBase
from typing import List
import copy
import random  # aleatorio


class QuickSort(AlgoritmoBase):
    THRESHOLD = 16  ## para usarlo en subarreglos pequeños

    @AlgoritmoBase.timer_decorator
    def sort(self, array: List[int]) -> List[int]:
        """QuickSort"""
        self.input_array = array
        self.iterations = 0
        self.output_array = copy.deepcopy(self.input_array)
        self.insertion_calls = 0  ## para ver cuantas veces se uso el insertion.

        if len(self.output_array) <= 1:
            return self.output_array

        self._quicksort(0, len(self.output_array) - 1)
        return self.output_array

    def _quicksort(self, low: int, high: int) -> None:
        ##si el subarreglo es pequeño, usamos insertion sort.
        if high - low + 1 <= self.THRESHOLD:
            self._insertion(low, high)
            return

        if low < high:
            p = self._partition(low, high)
            self._quicksort(low, p - 1)
            self._quicksort(p + 1, high)

    def _partition(self, low: int, high: int) -> int:
        pivot_idx = random.randint(low, high)
        if pivot_idx != high:
            self.output_array[pivot_idx], self.output_array[high] = (
                self.output_array[high],
                self.output_array[pivot_idx],
            )

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

    def _insertion(self, low: int, high: int) -> None:
        ##Insertion sort sobre el rango [low, high] (incluido).
        self.insertion_calls += 1  # opcional
        arr = self.output_array
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            # contamos comparación cada vez que chequeamos arr[j] > key
            while j >= low and arr[j] > key:
                self.iterations += 1
                arr[j + 1] = arr[j]
                j -= 1
            # una comparación más si salió porque falló (opcional):
            # if j >= low: self.iterations += 1
            arr[j + 1] = key
