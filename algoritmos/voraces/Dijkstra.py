import heapq  # para usar la cola de prioridad (más eficiente)


def dijkstra(grafo, inicio):
    distancias = {
        nodo: float("inf") for nodo in grafo
    }  # todas las distancias son infinitas
    distancias[inicio] = 0  # la distancia al inicio es 0
    cola = [(0, inicio)]  # (distancia, nodo)

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si encontramos una distancia mayor, la ignoramos
        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            # Si encontramos un camino más corto
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola, (distancia, vecino))

    return distancias


def main():
    # Grafo de ejemplo
    grafo = {
        "A": {"B": 2, "C": 5},
        "B": {"A": 2, "C": 6, "D": 1},
        "C": {"A": 5, "B": 6, "D": 3},
        "D": {"B": 1, "C": 3},
    }

    resultado = dijkstra(grafo, "A")
    print(resultado)


if __name__ == "__main__":
    main()
