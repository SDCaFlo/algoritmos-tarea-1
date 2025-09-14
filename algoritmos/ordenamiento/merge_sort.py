from .base import AlgoritmoBase
from typing import List


class MergeSort(AlgoritmoBase):
    @AlgoritmoBase.timer_decorator
    def sort(self, array: List[int], ascending: bool = True) -> List[int]:
        """BubbleSort"""
        self.input_array = array
        self.output_array = mergeSort(array)

        return self.output_array


def mergeSort(array: list):
    # division del array
    length = len(array)
    # condicion de salida
    if length <= 1:
        return array
    index = length // 2
    left_array = array[:index]
    right_array = array[index:]

    # ordenamos ambas mitades
    left_sorted = mergeSort(left_array)
    right_sorted = mergeSort(right_array)

    # combinacion de mitades ordenadas
    return sort(left_sorted, right_sorted)


def sort(left_array, right_array):
    # vamos a comparar índice por índice. seteamos ambos en 0
    left_index, right_index = 0, 0

    # inicializamos el array con 0 elementos
    merged_array = []

    # bucle de comparación
    while left_index < len(left_array) and right_index < len(right_array):
        left_value = left_array[left_index]
        right_value = right_array[right_index]
        # agregamos el menor valor
        if left_value < right_value:
            merged_array.append(left_value)
            left_index += 1
        else:
            merged_array.append(right_value)
            right_index += 1

    # si se sale del bucle, agregamos los valores restantes (que ya estan ordenados)
    merged_array.extend(left_array[left_index::])
    merged_array.extend(right_array[right_index::])

    return merged_array
