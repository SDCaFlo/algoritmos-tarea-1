# Algoritmo de Kruskal
class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        rx, ry = self.encontrar(x), self.encontrar(y)
        if rx != ry:
            self.padre[ry] = rx
            return True
        return False


def kruskal(n, aristas):
    uf = UnionFind(n)
    mst = []
    aristas.sort(key=lambda x: x[2])  # ordenar por peso

    for u, v, peso in aristas:
        if uf.unir(u, v):
            mst.append((u, v, peso))

    return mst


def main():
    # Nodos: A=0, B=1, C=2, D=3
    aristas = [
        (0, 1, 1),  # A-B
        (0, 2, 5),  # A-C
        (1, 2, 2),  # B-C
        (1, 3, 4),  # B-D
        (2, 3, 3),  # C-D
    ]

    resultado = kruskal(4, aristas)

    # Mostrar resultado con letras
    nodos = ["A", "B", "C", "D"]
    for u, v, peso in resultado:
        print(f"{nodos[u]} -- {nodos[v]} : {peso}")


if __name__ == "__main__":
    main()
