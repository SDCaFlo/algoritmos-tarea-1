"""Clases asociadas a las fichas de ajedrez"""


class TableroAjedrez:
    """Representa un tablero de ajedrez"""

    x_size = 8
    y_size = 8

    @classmethod
    def possible_positions(cls):
        # retorna las distintas posiciones posibles del tablero en formato tupla desde(1,1) hasta (8,8),
        return [
            (x, y) for x in range(1, cls.x_size + 1) for y in range(1, cls.y_size + 1)
        ]


class Ficha:
    """Representa una ficha dentro del tablero"""

    def __init__(self, x, y):
        # Inicializamos la ficha en la posición x,y
        if (x, y) in TableroAjedrez.possible_positions():
            self.posicion = (x, y)
            self.ruta_actual = [(x, y)]
        else:
            raise self.MovimientoIlegal

    def __str__(self):
        return f"Posición: {self.posicion}"

    def posibles_movimientos(self):
        return

    def mover(self):
        return

    def deshacer(self):
        self.ruta_actual.pop()
        self.posicion = self.ruta_actual[-1]

    class MovimientoIlegal(Exception):
        # Error para movimientos no posibles
        pass


class Caballo(Ficha):
    """Representa la ficha de caballo."""

    # patron movimiento de la ficha
    patron_movimiento = [
        (x, y) for x in [-1, 1, -2, 2] for y in [-1, 1, -2, 2] if abs(x) != abs(y)
    ]

    def posibles_movimientos(self):
        # analiza los posibles movimientos de la ficha
        return [
            (self.posicion[0] + movimiento[0], self.posicion[1] + movimiento[1])
            for movimiento in self.patron_movimiento
            if (self.posicion[0] + movimiento[0], self.posicion[1] + movimiento[1])
            in TableroAjedrez.possible_positions()
        ]

    def mover(self, x, y):
        if (x, y) in self.posibles_movimientos():
            self.posicion = (x, y)
            self.ruta_actual.append((x, y))
            return self
        else:
            raise self.MovimientoIlegal
