from .base import AlgoritmoBase


class InsertionSort(AlgoritmoBase):
    @AlgoritmoBase.timer_decorator
    def sort(self, lista):
        arr = lista.copy()

        # Recorremos la lista desde el segundo elemento hasta el final
        for i in range(1, len(arr)):
            clave = arr[
                i
            ]  # Guardamos el valor actual (el que queremos insertar en la posición correcta)
            j = i - 1  # Empezamos a comparar con los elementos anteriores

            # Mientras no lleguemos al inicio de la lista y el elemento anterior sea mayor que la clave
            while j >= 0 and arr[j] > clave:
                arr[j + 1] = arr[j]  # Desplazamos el elemento hacia la derecha
                j -= 1  # Seguimos comparando con el siguiente elemento a la izquierda

            arr[j + 1] = clave  # Insertamos la clave en su posición ordenada

        return arr  # Devolvemos la lista ya ordenada
