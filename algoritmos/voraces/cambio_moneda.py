def calcular_cambio(monedas, monto):
    # Ordenamos las monedas de mayor a menor
    monedas.sort(reverse=True)
    resultado = []

    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)

    return resultado


def main():
    monedas = [25, 10, 5, 1]  # Puedes cambiar estas monedas si lo deseas

    try:
        monto = int(input("Ingrese el monto a cambiar: "))
        if monto > 0:
            resultado = calcular_cambio(monedas, monto)

            print(f"\nCambio para {monto}:")
            print(" ".join(map(str, resultado)))
            print(f"\nTotal de monedas usadas: {len(resultado)}")
        else:
            print("Monto inválido. Debe ser un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")


if __name__ == "__main__":
    main()
