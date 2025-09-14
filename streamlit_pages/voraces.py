import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# Importar tus algoritmos
from algoritmos.voraces.Kruskal import kruskal
from algoritmos.voraces.Dijkstra import dijkstra
from algoritmos.voraces.agente_viajero import calcular_ruta_voraz
from algoritmos.voraces.cambio_moneda import calcular_cambio


def mostrar():
    # ========================
    # Interfaz principal
    # ========================
    st.set_page_config(page_title="Algoritmos Voraces", layout="centered")
    st.title("⚡ Algoritmos Voraces")

    opcion = st.radio(
        "Selecciona un algoritmo:",
        ["Kruskal", "Dijkstra", "Agente Viajero", "Cambio de Moneda"],
    )

    # ========================
    # Algoritmo de Kruskal
    # ========================
    if opcion == "Kruskal":
        st.subheader("🌳 Árbol de Expansión Mínima (Kruskal)")

        # Grafo de ejemplo
        aristas = [
            (0, 1, 1),
            (0, 2, 5),
            (1, 2, 2),
            (1, 3, 4),
            (2, 3, 3),
        ]
        nodos = ["A", "B", "C", "D"]

        if st.button("Ejecutar Kruskal"):
            mst = kruskal(4, aristas)
            st.success("Árbol de expansión mínima encontrado")
            for u, v, peso in mst:
                st.write(f"{nodos[u]} -- {nodos[v]} : {peso}")

            # Visualización
            G = nx.Graph()
            G.add_weighted_edges_from(aristas)
            pos = nx.spring_layout(G)

            plt.figure(figsize=(5, 5))
            nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1500)
            nx.draw_networkx_edge_labels(
                G, pos, edge_labels={(u, v): w for u, v, w in aristas}
            )
            nx.draw_networkx_edges(G, pos, edgelist=mst, width=3, edge_color="red")
            st.pyplot(plt)

    # ========================
    # Algoritmo de Dijkstra
    # ========================
    elif opcion == "Dijkstra":
        st.subheader("📍 Rutas más cortas (Dijkstra)")

        grafo = {
            "A": {"B": 2, "C": 5},
            "B": {"A": 2, "C": 6, "D": 1},
            "C": {"A": 5, "B": 6, "D": 3},
            "D": {"B": 1, "C": 3},
        }
        inicio = st.selectbox("Selecciona nodo inicial", list(grafo.keys()))

        if st.button("Ejecutar Dijkstra"):
            distancias = dijkstra(grafo, inicio)
            st.write("Distancias mínimas desde", inicio)
            st.json(distancias)

    # ========================
    # Algoritmo Agente Viajero
    # ========================
    elif opcion == "Agente Viajero":
        st.subheader("🧳 Problema del Viajero (Greedy)")

        distancias = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0],
        ]
        nombres_ciudades = ["A", "B", "C", "D"]

        inicio = st.selectbox(
            "Ciudad inicial",
            list(range(len(nombres_ciudades))),
            format_func=lambda x: nombres_ciudades[x],
        )

        if st.button("Ejecutar Agente Viajero"):
            ruta, costo_total = calcular_ruta_voraz(distancias, inicio)
            st.success(f"Costo total: {costo_total}")

            for i in range(len(ruta) - 1):
                st.write(
                    f"{nombres_ciudades[ruta[i]]} → {nombres_ciudades[ruta[i + 1]]} (costo {distancias[ruta[i]][ruta[i + 1]]})"
                )

    # ========================
    # Algoritmo Cambio de Moneda
    # ========================
    elif opcion == "Cambio de Moneda":
        st.subheader("💰 Cambio de Monedas (Greedy)")

        monedas = st.text_input("Monedas disponibles (separadas por coma)", "25,10,5,1")
        monedas = [int(x) for x in monedas.split(",")]
        monto = st.number_input("Monto a cambiar", min_value=1, value=87)

        if st.button("Calcular cambio"):
            resultado = calcular_cambio(monedas, monto)
            st.success(f"Cambio para {monto}: {resultado}")
            st.write(f"Total de monedas usadas: {len(resultado)}")
