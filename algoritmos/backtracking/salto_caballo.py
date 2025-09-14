from .utils.ajedrez import TableroAjedrez, Caballo


def salto_caballo(ficha: Caballo = Caballo(1, 1)):
    # Revisamos si ya se realizaron 64 movimientos ( Si la ficha ya pasó por todas las casillas)
    if len(ficha.ruta_actual) == TableroAjedrez.x_size * TableroAjedrez.y_size:
        return True, ficha

    # Analizamos los posibles movimientos de la ficha desde nuestra posición actual
    posibles_movimientos = [
        movimiento
        for movimiento in ficha.posibles_movimientos()
        if movimiento not in ficha.ruta_actual
    ]

    # heuristica_warnsdorff -> Optimiza Búsqueda
    movimientos_ordenados = sorted(
        [
            (
                movimiento,
                len(
                    [
                        m
                        for m in Caballo(*movimiento).posibles_movimientos()
                        if m not in ficha.ruta_actual
                    ]
                ),
            )
            for movimiento in posibles_movimientos
        ],
        key=lambda m: m[1],
    )

    for movimiento, _ in movimientos_ordenados:
        ficha.mover(*movimiento)  # movemos a la siguiente casilla
        solucion, ficha = salto_caballo(ficha)  # Ejecutamos la lógica recursiva

        if solucion:
            return True, ficha  # Verificamos si encontramos la solución

        ficha.deshacer()  # Si es un camino sin salida, regresamos.

    return False, ficha
