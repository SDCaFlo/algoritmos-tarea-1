from .base import AlgoritmoBase
from typing import List
import copy


class BubbleSort(AlgoritmoBase):
    @AlgoritmoBase.timer_decorator
    def sort(self, array: List[int], ascending: bool = True) -> List[int]:
        """BubbleSort"""
        self.input_array = array
        self.output_array = copy.deepcopy(
            self.input_array
        )  # creamos una copia sin referencia.

        n = len(array)  # capturamos la longitud del array

        for i in range(n):
            for j in range(n - 1):
                if (
                    self.output_array[j] > self.output_array[j + 1]
                ):  # evaluamos si el elemento es mayor
                    helper_var = self.output_array[j]
                    self.output_array[j] = self.output_array[j + 1]
                    self.output_array[j + 1] = helper_var
                self.iterations += 1

        return self.output_array
