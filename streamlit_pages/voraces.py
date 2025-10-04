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
    st.set_page_config(page_title="Algoritmos Voraces", layout="wide")
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
        if "kruskal_nodos" not in st.session_state:
            st.session_state.kruskal_nodos = ["A", "B", "C", "D"]
        if "kruskal_aristas" not in st.session_state:
            st.session_state.kruskal_aristas = [
                (0, 1, 1),
                (0, 2, 5),
                (1, 2, 2),
                (1, 3, 4),
                (2, 3, 3),
            ]

        st.write("### Nodos")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("Nodos actuales:", st.session_state.kruskal_nodos)
            new_node = st.text_input("Agregar nodo", "")
            if st.button("Añadir nodo"):
                if new_node and new_node not in st.session_state.kruskal_nodos:
                    st.session_state.kruskal_nodos.append(new_node)
                    st.rerun()
        with col2:
            remove_node = st.selectbox("Eliminar nodo", st.session_state.kruskal_nodos)
            if st.button("Eliminar nodo"):
                idx = st.session_state.kruskal_nodos.index(remove_node)
                st.session_state.kruskal_nodos.remove(remove_node)
                # Remove edges related to this node
                st.session_state.kruskal_aristas = [
                    (u, v, w) for u, v, w in st.session_state.kruskal_aristas
                    if u != idx and v != idx
                ]
                # Reindex edges
                def reindex(i):
                    return i - 1 if i > idx else i
                st.session_state.kruskal_aristas = [
                    (reindex(u), reindex(v), w) for u, v, w in st.session_state.kruskal_aristas
                ]
                st.rerun()

        st.write("### Aristas")
        col3, col4 = st.columns([2, 1])
        with col3:
            st.write("Aristas actuales:")
            for idx, (u, v, w) in enumerate(st.session_state.kruskal_aristas):
                st.write(f"{st.session_state.kruskal_nodos[u]} -- {st.session_state.kruskal_nodos[v]} : {w}")
        with col4:
            origen = st.selectbox("Origen", st.session_state.kruskal_nodos)
            destino = st.selectbox("Destino", st.session_state.kruskal_nodos)
            peso = st.number_input("Peso", value=1)
            if st.button("Añadir arista"):
                u = st.session_state.kruskal_nodos.index(origen)
                v = st.session_state.kruskal_nodos.index(destino)
                if u != v:
                    st.session_state.kruskal_aristas.append((u, v, peso))
                    st.rerun()
            arista_idx = st.number_input("Índice arista a eliminar", min_value=0, max_value=max(0, len(st.session_state.kruskal_aristas)-1), value=0)
            if st.button("Eliminar arista"):
                if st.session_state.kruskal_aristas:
                    st.session_state.kruskal_aristas.pop(arista_idx)
                    st.rerun()

        if st.button("Ejecutar Kruskal"):
            n = len(st.session_state.kruskal_nodos)
            mst = kruskal(n, st.session_state.kruskal_aristas)
            st.success("Árbol de expansión mínima encontrado")
            for u, v, peso in mst:
                st.write(f"{st.session_state.kruskal_nodos[u]} -- {st.session_state.kruskal_nodos[v]} : {peso}")

            # Visualización
            G = nx.Graph()
            G.add_weighted_edges_from(st.session_state.kruskal_aristas)
            pos = nx.spring_layout(G)

            plt.figure(figsize=(5, 5))
            nx.draw(G, pos, with_labels=True, labels={i: name for i, name in enumerate(st.session_state.kruskal_nodos)}, node_color="skyblue", node_size=1500)
            nx.draw_networkx_edge_labels(
                G, pos, edge_labels={(u, v): w for u, v, w in st.session_state.kruskal_aristas}
            )
            nx.draw_networkx_edges(G, pos, edgelist=mst, width=3, edge_color="red")
            st.pyplot(plt)

    # ========================
    # Algoritmo de Dijkstra
    # ========================
    elif opcion == "Dijkstra":
        st.subheader("📍 Rutas más cortas (Dijkstra)")

        # Estado inicial
        if "dijkstra_nodos" not in st.session_state:
            st.session_state.dijkstra_nodos = ["A", "B", "C", "D"]
        if "dijkstra_aristas" not in st.session_state:
            st.session_state.dijkstra_aristas = [
                {"origen": "A", "destino": "B", "costo": 2},
                {"origen": "A", "destino": "C", "costo": 5},
                {"origen": "B", "destino": "C", "costo": 6},
                {"origen": "B", "destino": "D", "costo": 1},
                {"origen": "C", "destino": "D", "costo": 3},
                {"origen": "D", "destino": "B", "costo": 1},
                {"origen": "D", "destino": "C", "costo": 3},
            ]

        st.write("### Nodos")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("Nodos actuales:", st.session_state.dijkstra_nodos)
            new_node = st.text_input("Agregar nodo", "")
            if st.button("Añadir nodo"):
                if new_node and new_node not in st.session_state.dijkstra_nodos:
                    st.session_state.dijkstra_nodos.append(new_node)
                    st.rerun()
        with col2:
            remove_node = st.selectbox("Eliminar nodo", st.session_state.dijkstra_nodos)
            if st.button("Eliminar nodo"):
                st.session_state.dijkstra_nodos.remove(remove_node)
                # Eliminar aristas relacionadas
                st.session_state.dijkstra_aristas = [
                    a for a in st.session_state.dijkstra_aristas
                    if a["origen"] != remove_node and a["destino"] != remove_node
                ]
                st.rerun()

        st.write("### Aristas")
        col3, col4 = st.columns([2, 1])
        with col3:
            st.write("Aristas actuales:")
            for idx, a in enumerate(st.session_state.dijkstra_aristas):
                st.write(f"{a['origen']} → {a['destino']} : {a['costo']}")
        with col4:
            origen = st.selectbox("Origen", st.session_state.dijkstra_nodos)
            destino = st.selectbox("Destino", st.session_state.dijkstra_nodos)
            costo = st.number_input("Costo", value=1)
            if st.button("Añadir arista"):
                if origen != destino:
                    st.session_state.dijkstra_aristas.append({"origen": origen, "destino": destino, "costo": costo})
                    st.rerun()
            arista_idx = st.number_input("Índice arista a eliminar", min_value=0, max_value=max(0, len(st.session_state.dijkstra_aristas)-1), value=0)
            if st.button("Eliminar arista"):
                if st.session_state.dijkstra_aristas:
                    st.session_state.dijkstra_aristas.pop(arista_idx)
                    st.rerun()

        # Construir el grafo para Dijkstra
        grafo = {n: {} for n in st.session_state.dijkstra_nodos}
        for a in st.session_state.dijkstra_aristas:
            grafo[a["origen"]][a["destino"]] = int(a["costo"])

        inicio = st.selectbox("Selecciona nodo inicial", st.session_state.dijkstra_nodos)

        if st.button("Ejecutar Dijkstra"):
            distancias = dijkstra(grafo, inicio)
            st.write("Distancias mínimas desde", inicio)
            st.json(distancias)

            # Visualización
            G = nx.DiGraph()
            for a in st.session_state.dijkstra_aristas:
                G.add_edge(a["origen"], a["destino"], weight=a["costo"])
            pos = nx.spring_layout(G)
            plt.figure(figsize=(5, 5))
            nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=1500)
            nx.draw_networkx_edge_labels(
                G, pos, edge_labels={(a["origen"], a["destino"]): a["costo"] for a in st.session_state.dijkstra_aristas}
            )
            st.pyplot(plt)
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

        G = nx.Graph()
        for i in range(len(nombres_ciudades)):
            for j in range(len(nombres_ciudades)):
                if i != j:
                    G.add_edge(nombres_ciudades[i], nombres_ciudades[j], weight=distancias[i][j])
        pos = nx.spring_layout(G)
        plt.figure(figsize=(5, 5))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1200)
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels={(nombres_ciudades[i], nombres_ciudades[j]): distancias[i][j]
                                for i in range(len(nombres_ciudades)) for j in range(len(nombres_ciudades)) if i != j}
        )

        inicio = st.selectbox(
            "Ciudad inicial",
            list(range(len(nombres_ciudades))),
            format_func=lambda x: nombres_ciudades[x],
        )

        ruta_edges = []
        if st.button("Ejecutar Agente Viajero"):
            ruta, costo_total = calcular_ruta_voraz(distancias, inicio)
            st.success(f"Costo total: {costo_total}")
            for i in range(len(ruta) - 1):
                st.write(
                    f"{nombres_ciudades[ruta[i]]} → {nombres_ciudades[ruta[i + 1]]} (costo {distancias[ruta[i]][ruta[i + 1]]})"
                )
            ruta_edges = [(nombres_ciudades[ruta[i]], nombres_ciudades[ruta[i + 1]]) for i in range(len(ruta) - 1)]

        # Si hay ruta, dibujarla en rojo sobre el mismo grafo
        if ruta_edges:
            nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, width=4, edge_color="red")

        st.pyplot(plt)
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
