import streamlit as st
import pandas as pd
import numpy as np
from algoritmos.programacion_dinamica.floyd import Grafo, FloydMatrix
from algoritmos.programacion_dinamica.mochila import Elemento, calcular_matriz_mochila, calcular_elementos_incluidos

def floyd_app():
    st.subheader("Algoritmo de Floyd (Caminos mínimos)")
    # Estado para nodos y aristas
    if "floyd_nodos" not in st.session_state:
        st.session_state.floyd_nodos = ["A", "B", "C", "D"]
    if "floyd_aristas" not in st.session_state:
        st.session_state.floyd_aristas = [
            {"origen": "A", "destino": "B", "costo": 2},
            {"origen": "A", "destino": "D", "costo": 3},
            {"origen": "B", "destino": "A", "costo": 3},
            {"origen": "B", "destino": "C", "costo": 2},
            {"origen": "C", "destino": "D", "costo": 4},
            {"origen": "D", "destino": "A", "costo": -2},
            {"origen": "D", "destino": "B", "costo": 6},
        ]

    st.write("### Nodos")
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("Nodos actuales:", st.session_state.floyd_nodos)
        new_node = st.text_input("Agregar nodo", "")
        if st.button("Añadir nodo"):
            if new_node and new_node not in st.session_state.floyd_nodos:
                st.session_state.floyd_nodos.append(new_node)
                st.rerun()
    with col2:
        remove_node = st.selectbox("Eliminar nodo", st.session_state.floyd_nodos)
        if st.button("Eliminar nodo"):
            st.session_state.floyd_nodos.remove(remove_node)
            # Eliminar aristas relacionadas
            st.session_state.floyd_aristas = [
                a for a in st.session_state.floyd_aristas
                if a["origen"] != remove_node and a["destino"] != remove_node
            ]
            st.rerun()

    st.write("### Aristas")
    col3, col4 = st.columns([2,1])
    with col3:
        st.write("Aristas actuales:")
        for idx, a in enumerate(st.session_state.floyd_aristas):
            st.write(f"{a['origen']} → {a['destino']} : {a['costo']}")
    with col4:
        origen = st.selectbox("Origen", st.session_state.floyd_nodos)
        destino = st.selectbox("Destino", st.session_state.floyd_nodos)
        costo = st.number_input("Costo", value=1)
        if st.button("Añadir arista"):
            if origen != destino:
                st.session_state.floyd_aristas.append({"origen": origen, "destino": destino, "costo": costo})
                st.rerun()
        arista_idx = st.number_input("Índice arista a eliminar", min_value=0, max_value=max(0, len(st.session_state.floyd_aristas)-1), value=0)
        if st.button("Eliminar arista"):
            if st.session_state.floyd_aristas:
                st.session_state.floyd_aristas.pop(arista_idx)
                st.rerun()

    if st.button("Resolver Floyd"):
        grafo = Grafo()
        for n in st.session_state.floyd_nodos:
            grafo.agregar_nodo(n)
        for a in st.session_state.floyd_aristas:
            grafo.agregar_arista(a["origen"], a["destino"], int(a["costo"]))
        floyd = FloydMatrix(grafo)
        floyd.solve_matrix()
        node_names = [n for n in st.session_state.floyd_nodos]
        # Convert numpy matrices to pandas DataFrames with node names as labels
        route_df = pd.DataFrame(floyd.route_matrix, index=node_names, columns=node_names)
        cost_df = pd.DataFrame(floyd.cost_matrix, index=node_names, columns=node_names)
        st.write("#### Matriz de rutas y costos")
        st.write("Rutas:")
        st.dataframe(route_df)
        st.write("Costos:")
        st.dataframe(cost_df)

def mochila_app():
    st.subheader("Algoritmo de la Mochila (Knapsack)")
    # Estado para elementos y capacidad
    if "mochila_elementos" not in st.session_state:
        st.session_state.mochila_elementos = [
            {"nombre": "A", "valor": 2, "peso": 3},
            {"nombre": "B", "valor": 2, "peso": 1},
            {"nombre": "C", "valor": 4, "peso": 3},
            {"nombre": "D", "valor": 5, "peso": 4},
            {"nombre": "E", "valor": 3, "peso": 2},
        ]
    if "mochila_capacidad" not in st.session_state:
        st.session_state.mochila_capacidad = 7

    st.write("### Elementos")
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("Elementos actuales:")
        for idx, e in enumerate(st.session_state.mochila_elementos):
            st.write(f"{e['nombre']}: valor={e['valor']}, peso={e['peso']}")
    with col2:
        nombre = st.text_input("Nombre", value=chr(65+len(st.session_state.mochila_elementos)%26))
        valor = st.number_input("Valor", value=1)
        peso = st.number_input("Peso", value=1)
        if st.button("Añadir elemento"):
            st.session_state.mochila_elementos.append({"nombre": nombre, "valor": int(valor), "peso": int(peso)})
            st.rerun()
        elem_idx = st.number_input("Índice elemento a eliminar", min_value=0, max_value=max(0, len(st.session_state.mochila_elementos)-1), value=0)
        if st.button("Eliminar elemento"):
            if st.session_state.mochila_elementos:
                st.session_state.mochila_elementos.pop(elem_idx)
                st.rerun()

    capacidad = st.number_input("Capacidad de la mochila", min_value=1, value=st.session_state.mochila_capacidad)
    st.session_state.mochila_capacidad = capacidad

    if st.button("Resolver Mochila"):
        elementos = [Elemento(e["valor"], e["peso"]) for e in st.session_state.mochila_elementos]
        nom_elementos = [e['nombre'] for e in st.session_state.mochila_elementos]
        nom_elementos.insert(0, "-")
        matrix = calcular_matriz_mochila(elementos, int(capacidad))
        st.write("#### Matriz de solución")
        st.dataframe(pd.DataFrame(data=matrix, index=nom_elementos))
        incluidos = calcular_elementos_incluidos(elementos, matrix)
        st.write("#### Elementos incluidos (óptimos):")
        for e in incluidos:
            idx = elementos.index(e)
            st.write(f"{st.session_state.mochila_elementos[idx]['nombre']}: valor={e.valor}, peso={e.peso}")

def mostrar():
    st.title("Algoritmos Dinámicos Interactivos")
    opcion = st.radio("Selecciona algoritmo:", ["floyd", "mochila"])
    if opcion == "floyd":
        floyd_app()
    elif opcion == "mochila":
        mochila_app()