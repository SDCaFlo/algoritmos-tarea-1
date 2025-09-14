def hanoi(n, origen, destino, auxiliar, movimientos):
    # Caso base: un solo disco
    if n == 1:
        movimientos.append((origen, destino))
        return

    # Paso 1: mover n-1 discos al auxiliar
    hanoi(n - 1, origen, auxiliar, destino, movimientos)

    # Paso 2: mover el disco más grande al destino
    movimientos.append((origen, destino))

    # Paso 3: mover n-1 discos del auxiliar al destino
    hanoi(n - 1, auxiliar, destino, origen, movimientos)


def main():
    # Ejemplo
    movs = []
    hanoi(3, "A", "C", "B", movs)

    print("Movimientos:")
    for i, (o, d) in enumerate(movs, 1):
        print(f"{i}. {o} -> {d}")


if __name__ == "__main__":
    main()

