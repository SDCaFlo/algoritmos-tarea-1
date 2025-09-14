from .base import AlgoritmoBase
from typing import List


class BusquedaBinaria(AlgoritmoBase):
    @AlgoritmoBase.timer_decorator
    def search(self, array: List[int], target: int, auto_sort: bool = True) -> int:
        """
        Búsqueda binaria iterativa.
        """
        self.input_array = array
        self.iterations = 0
        # Usamos un array ordenado para garantizar la precondición de la búsqueda...
        self.output_array = sorted(array) if auto_sort else array[:]

        lo, hi = 0, len(self.output_array) - 1
        self.found_index = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            self.iterations += 1

            if self.output_array[mid] == target:
                self.found_index = mid
                return mid
            elif self.output_array[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
