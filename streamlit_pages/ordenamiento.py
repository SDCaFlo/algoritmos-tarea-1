from algoritmos.ordenamiento import (
    BubbleSort,
    MergeSort,
    SelectionSort,
    QuickSort,
    InsertionSort,
    BusquedaBinaria,
)
import streamlit as st
import random


def mostrar():
    st.title("Algoritmos de ordenamiento")

    # Opción para generar arrays aleatorios
    col1, col2 = st.columns([2, 1])
    with col2:
        size = st.selectbox("Tamaño del array aleatorio", (10, 50, 100))
        if st.button("Generar array aleatorio"):
            array = [random.randint(0, 100) for _ in range(size)]
            st.session_state["array"] = array
        else:
            array = st.session_state.get("array", [5, 4, 3, 2])

    with col1:
        text_array = st.text_input(
            "Ingresa los números separados por comas", ",".join(map(str, array))
        )
        try:
            array = [int(x) for x in text_array.split(",") if x.strip() != ""]
            st.session_state["array"] = array
        except Exception:
            st.error("Asegúrese de que los números estén separados por comas")
            array = []

    ##para busqueda binaria pedimos lo que se va a ejecutar

    algorithm = st.selectbox(
        "Selecciona el método de ordenamiento:",
        (
            "Bubble Sort",
            "Merge Sort",
            "Selection Sort",
            "Quick Sort",
            "Insertion Sort",
            "Busqueda Binaria",
        ),
    )

    ##para busqueda binaria pedimos lo que se va a ejecutar
    target = None
    if algorithm == "Busqueda Binaria":
        target = st.number_input("Valor a buscar:", value=5, step=1, format="%d")

    # Botón para ejecutar
    if st.button("Ordenar/Buscar"):
        if array:
            if algorithm == "Bubble Sort":
                sorter = BubbleSort()
            elif algorithm == "Merge Sort":
                sorter = MergeSort()
            elif algorithm == "Selection Sort":
                sorter = SelectionSort()
            elif algorithm == "Quick Sort":
                sorter = QuickSort()
            elif algorithm == "Insertion Sort":
                sorter = InsertionSort()
            elif algorithm == "Busqueda Binaria":
                searcher = BusquedaBinaria()
                sorter = QuickSort()
                idx = searcher.search(array, int(target), auto_sort=True)
                if idx != -1:
                    st.success(f"Encontrado: {int(target)} en indice {idx}")
                else:
                    st.warning(f"No se encontro el valor {int(target)}")

            sorted_array = sorter.sort(array)
            st.success(f"Array Ordenado: {sorted_array}")
        else:
            st.warning("⚠️ Ingresa un array válido para ordenar.")
