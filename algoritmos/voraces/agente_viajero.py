def calcular_ruta_voraz(distancias, ciudad_inicial):
    n = len(distancias)
    visitado = [False] * n
    ruta = []

    ciudad_actual = ciudad_inicial
    ruta.append(ciudad_actual)
    visitado[ciudad_actual] = True
    costo_total = 0

    for _ in range(1, n):
        siguiente_ciudad = -1
        distancia_minima = float("inf")

        for j in range(n):
            if not visitado[j] and distancias[ciudad_actual][j] < distancia_minima:
                siguiente_ciudad = j
                distancia_minima = distancias[ciudad_actual][j]

        costo_total += distancia_minima
        ciudad_actual = siguiente_ciudad
        ruta.append(ciudad_actual)
        visitado[ciudad_actual] = True

    # Volver al punto de inicio
    ruta.append(ciudad_inicial)
    costo_total += distancias[ciudad_actual][ciudad_inicial]

    return ruta, costo_total


def main():
    # Matriz de distancias (simétrica)
    distancias = [
        # A   B   C   D
        [0, 10, 15, 20],  # A
        [10, 0, 35, 25],  # B
        [15, 35, 0, 30],  # C
        [20, 25, 30, 0],  # D
    ]

    nombres_ciudades = ["A", "B", "C", "D"]
    ciudad_inicial = 0

    ruta, costo_total = calcular_ruta_voraz(distancias, ciudad_inicial)

    print("Ruta recorrida:\n")
    for i in range(len(ruta) - 1):
        ciudad_desde = ruta[i]
        ciudad_hacia = ruta[i + 1]
        costo = distancias[ciudad_desde][ciudad_hacia]
        print(
            f"{nombres_ciudades[ciudad_desde]} -> {nombres_ciudades[ciudad_hacia]} (costo: {costo})"
        )

    print(f"\nCosto total del recorrido: {costo_total}")


if __name__ == "__main__":
    main()
