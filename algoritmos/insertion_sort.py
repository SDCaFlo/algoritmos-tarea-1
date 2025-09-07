from .base import AlgoritmoBase


class InsertionSort(AlgoritmoBase):
    @AlgoritmoBase.timer_decorator
    def sort(self, lista):
        arr = lista.copy()
        for i in range(1, len(arr)):
            clave = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > clave:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = clave
        return arr
