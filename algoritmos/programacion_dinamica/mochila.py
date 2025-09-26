import numpy as np


class Elemento:
    """Clase elemento que almacena valor y peso"""

    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso


# Funciones
def calcular_matriz_mochila(
    lista_elementos: list[Elemento], capacidad: int
) -> np.ndarray:
    """Calcula una matriz de numpy con el algoritmo de la mochila"""
    # inicializamos matriz en numpy
    matrix = np.zeros(shape=(len(lista_elementos) + 1, capacidad + 1), dtype=np.int16)

    # Recorremos matriz
    for i in range(matrix.shape[0]):  # Iteramos elementos
        if i != 0:
            elemento_actual = lista_elementos[i - 1]  # Asignamos elemento a evaluar
        for j in range(matrix.shape[1]):  # Iteramos capacidades
            capacidad_actual = j
            # Secuencias de escape
            if i == 0:
                break
            if j == 0:
                continue

            # Comparación
            if elemento_actual.peso <= capacidad_actual:
                valor_encima = matrix[i - 1, j]  # Elemento superior
                valor_desfasado = matrix[
                    i - 1, j - elemento_actual.peso
                ]  # Valor desfasado
                nuevo_valor = (
                    valor_desfasado + elemento_actual.valor
                )  # Calculo del posible nuevo mejor valor
                matrix[i, j] = max([valor_encima, nuevo_valor])  # Comparación
            else:
                matrix[i, j] = matrix[i - 1, j]  # Reemplazo con el mejor valor.
    return matrix


def calcular_elementos_incluidos(
    lista_elementos: list[Elemento], matrix: np.ndarray
) -> list[Elemento]:
    """Retorna una lista con los elementos a incluir, dada una matriz de solucion de la mochila"""
    # picking_items based on a matrix and an ElementList
    curr_row, curr_column = matrix.shape[0] - 1, matrix.shape[1] - 1

    # Inicializacion de elementos
    included_elements = []
    for element in lista_elementos[::-1]:
        if matrix[curr_row, curr_column] != matrix[curr_row - 1, curr_column]:
            included_elements.append(element)
            curr_column = curr_column - element.peso
        curr_row = curr_row - 1

    return included_elements


def mostrar_resultados(included_elements: list[Elemento]):
    """Muestra los elementos incluidos y el resultado del algoritmo de la mochila"""
    total_peso = 0
    total_valor = 0
    print("Resultado: \n")
    print("Elem\tPeso\tValor")
    for index, element in enumerate(included_elements):
        total_peso += element.peso
        total_valor += element.valor
        print(f"{index + 1}\t{element.peso}\t{element.valor}")
    print("Total Peso: ", total_peso)
    print("Total Valor: ", total_valor)


def main():
    ele_1 = Elemento(2, 3)
    ele_2 = Elemento(2, 1)
    ele_3 = Elemento(4, 3)
    ele_4 = Elemento(5, 4)
    ele_5 = Elemento(3, 2)

    lista_elementos = [ele_1, ele_2, ele_3, ele_4, ele_5]
    capacidad = 7

    print('Lista de objetos: \n')
    for objeto in [ {'objeto': f'objeto_{index+1}', 'valor': objeto.valor, 'peso': objeto.peso} for index, objeto in enumerate(lista_elementos)]:
        print(f'{objeto['objeto']}, valor: {objeto['valor']}, peso:{objeto['peso']}')
    
    print('\nCapacidad de la mochila: ', capacidad)

    print('\n********Solving********\n')
    solved_matrix = calcular_matriz_mochila(lista_elementos, capacidad)
    elementos_incluidos = calcular_elementos_incluidos(lista_elementos, solved_matrix)
    mostrar_resultados(elementos_incluidos)


if __name__ == "__main__":
    main()
