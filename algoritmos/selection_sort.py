from .base import AlgoritmoBase
from typing import List
import copy

class SelectionSort(AlgoritmoBase):
    @AlgoritmoBase.timer_decorator
    def sort(self, array: List[int], ascending: bool = True) -> List[int]:
        """Selection Sort"""

        self.input_array = copy.deepcopy(array) # guardamos el input

        n = len(array)

        for i in range(n-1): # loop principal
            min_index = i

            for j in range(i+1, n): # actualizamos el índice mínimo
                if array[j] < array[min_index]:
                    min_index = j
            
            # intercambio
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp

        self.output_array = array # guardamos el output

        return self.output_array