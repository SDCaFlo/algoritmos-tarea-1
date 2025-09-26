import numpy as np


class Node:
    def __init__(self, name: str):
        self.name = name
        self.aristas = {
            name: {"nodo": self, "costo": 0},
        }

    def agregar_arista(self, nodo: "Node", costo: int):
        if nodo.name == self.name:
            print("Ruta inválida")
        elif nodo.name in self.aristas.keys():
            self.aristas[nodo.name]["costo"] = costo
            print(f"Ruta actualizada: {self.name}->{nodo.name}:{costo}")
        else:
            self.aristas[nodo.name] = {"nodo": nodo, "costo": costo}
            print(f"Ruta creada: {self.name}->{nodo.name}:{costo}")


class Grafo:
    def __init__(self):
        self.nodos: list[Node] = []

    def agregar_nodo(self, name: str):
        if name in [nodo.name for nodo in self.nodos]:
            print(f"El nodo {name} ya existe.")
        else:
            self.nodos.append(Node(name))
            print(f"Nodo {name} agregado.")

    def agregar_arista(self, nodo_origen: str, nodo_destino: str, costo: int):
        nodos_dict = {nodo.name: nodo for nodo in self.nodos}
        if nodo_origen and nodo_destino in nodos_dict.keys():
            nodos_dict[nodo_origen].agregar_arista(nodos_dict[nodo_destino], costo)
        else:
            print("Nodo inexistente")

    def listar_rutas(self):
        """ejm. {'origen': 'a', 'destino': 'b', 'costo': 3}"""
        lista_rutas = []
        for nodo in self.nodos:
            # lista_rutas.extend([ {'destino': arista['nodo'], 'costo': arista['costo']} for arista in nodo.aristas])
            for nombre_arista, datos_arista in nodo.aristas.items():
                item = {
                    "origen": nodo.name,
                    "destino": nombre_arista,
                    "costo": datos_arista["costo"],
                }
                lista_rutas.append(item)
        return lista_rutas


class FloydMatrix:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.inicializar_matrix()

    def inicializar_matrix(self):
        """Inicializa la matriz"""
        a = len(self.grafo.nodos)
        self.cost_matrix = np.full((a, a), np.inf)
        self.route_matrix = np.full(shape=(a, a), fill_value="-", dtype=str)
        return self

    def solve_matrix(self):
        """Resuelve la matriz"""
        # Asignamos pesos iniciales
        for ruta in self.grafo.listar_rutas():
            row_name = ruta["origen"]
            col_name = ruta["destino"]
            row_idx, col_idx = self.translate_index(row_name, col_name)
            self.cost_matrix[row_idx, col_idx] = ruta["costo"]
            self.route_matrix[row_idx, col_idx] = ruta["origen"]

        # Iteramos
        for node in self.grafo.nodos:
            # Vamos a tomar un nodo pivote y evaluar la matriz resultante
            pivot = node.name
            pivoted_nodes = [
                node.name for node in self.grafo.nodos if node.name != pivot
            ]

            for piv_node_row in pivoted_nodes:
                for piv_node_col in pivoted_nodes:
                    if piv_node_row == piv_node_col:
                        continue
                    curr_value = self.get_matrix_element(
                        piv_node_row, piv_node_col, "cost"
                    )
                    candidate_cost = self.get_matrix_element(
                        piv_node_row, pivot, "cost"
                    ) + self.get_matrix_element(pivot, piv_node_col, "cost")

                    if candidate_cost < curr_value:
                        self.set_matrix_element(
                            candidate_cost, piv_node_row, piv_node_col, "cost"
                        )
                        self.set_matrix_element(
                            pivot, piv_node_row, piv_node_col, "route"
                        )

    def translate_index(self, row_node: str, column_node: str):
        """Utilidad para traducir índices de la matriz"""
        mapping = {nodo.name: index for index, nodo in enumerate(self.grafo.nodos)}
        return (mapping[row_node], mapping[column_node])

    def get_matrix_element(self, row_node: str, column_node: str, matrix: str):
        row_idx, col_idx = self.translate_index(row_node, column_node)
        if matrix == "cost":
            return self.cost_matrix[row_idx, col_idx]
        elif matrix == "route":
            return self.route_matrix[row_idx, col_idx]

    def set_matrix_element(self, value, row_node: str, column_node: str, matrix: str):
        row_idx, col_idx = self.translate_index(row_node, column_node)
        if matrix == "cost":
            self.cost_matrix[row_idx, col_idx] = value
        elif matrix == "route":
            self.route_matrix[row_idx, col_idx] = value


def main():
    grafo = Grafo()
    grafo.agregar_nodo("a")
    grafo.agregar_nodo("b")
    grafo.agregar_nodo("c")
    grafo.agregar_nodo("d")
    grafo.agregar_arista("a", "b", 2)
    grafo.agregar_arista("a", "d", 3)
    grafo.agregar_arista("b", "a", 3)
    grafo.agregar_arista("b", "c", 2)
    grafo.agregar_arista("c", "d", 4)
    grafo.agregar_arista("d", "a", -2)
    grafo.agregar_arista("d", "b", 6)

    floyd = FloydMatrix(grafo)

    floyd.solve_matrix()
    print(floyd.route_matrix)
    print(floyd.cost_matrix)


if __name__ == "__main__":
    main()
