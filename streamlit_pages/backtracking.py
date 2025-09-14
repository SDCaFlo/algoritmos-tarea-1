import streamlit as st
from algoritmos.backtracking.salto_caballo import salto_caballo
from algoritmos.backtracking.torres_hanoi import hanoi
from algoritmos.backtracking.utils.ajedrez import Caballo, TableroAjedrez


def mostrar():
    # --- Menú ---
    st.title("🎯 Algoritmos Interactivos")
    opcion = st.radio(
        "Selecciona un algoritmo:", ["Salto del Caballo", "Torres de Hanoi"]
    )

    # --- Salto del Caballo ---
    if opcion == "Salto del Caballo":
        st.subheader("♞ Salto del Caballo (Knight's Tour)")

        # Posición inicial
        x = st.number_input(
            "Fila inicial", min_value=1, max_value=TableroAjedrez.x_size, value=1
        )
        y = st.number_input(
            "Columna inicial", min_value=1, max_value=TableroAjedrez.y_size, value=1
        )

        if st.button("Ejecutar algoritmo"):
            caballo = Caballo(x, y)
            solucion, caballo = salto_caballo(caballo)

            if solucion:
                st.success("¡Ruta encontrada! ✅")
                st.write("Ruta del caballo:", caballo.ruta_actual)

                # Dibujar tablero
                import numpy as np
                import matplotlib.pyplot as plt

                tablero = np.zeros((TableroAjedrez.x_size, TableroAjedrez.y_size))
                for i, (fx, fy) in enumerate(caballo.ruta_actual):
                    tablero[fx - 1, fy - 1] = i + 1

                fig, ax = plt.subplots()
                ax.matshow(tablero, cmap="viridis")

                for (i, j), val in np.ndenumerate(tablero):
                    ax.text(j, i, int(val), ha="center", va="center", color="white")

                st.pyplot(fig)
            else:
                st.error("No se encontró solución 😢")

    # --- Torres de Hanoi ---
    elif opcion == "Torres de Hanoi":
        st.subheader("🏗️ Torres de Hanoi")

        n = st.slider("Número de discos", 1, 10, 3)
        if st.button("Resolver Hanoi"):
            movimientos = []
            hanoi(n, "A", "C", "B", movimientos)

            st.success(f"Resuelto en {len(movimientos)} movimientos")
            for i, (o, d) in enumerate(movimientos, 1):
                st.write(f"{i}. {o} → {d}")
