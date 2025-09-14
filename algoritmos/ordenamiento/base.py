from typing import List
import time


class AlgoritmoBase:
    """Clase base para la posterior creacion de algoritmos"""

    def __init__(self):
        self.input_array: List[int] = []  # entrada (array desordenado)
        self.iterations: int = 0  # cantidad de iteraciones
        self.output_array: List[int] = []  # salida (array ordenado)
        self.execution_time: float = 0.0  # tiempo de ejecución

    @staticmethod
    def timer_decorator(func):
        def wrapper(self, *args, **kwargs):
            init_time = time.time()
            result = func(self, *args, **kwargs)
            end_time = time.time()
            self.execution_time = end_time - init_time
            return result

        return wrapper

    @timer_decorator
    def sort(self, array: List[int]) -> List[int]:
        time.sleep(1)
