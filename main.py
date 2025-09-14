from algoritmos.ordenamiento import BubbleSort, MergeSort, SelectionSort, QuickSort, InsertionSort
import streamlit as st
import random

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

algorithm = st.selectbox(
    "Selecciona el método de ordenamiento:",
    ("Bubble Sort", "Merge Sort", "Selection Sort", "Quick Sort", "Insertion Sort"),
)

# Botón para ejecutar
if st.button("Ordenar"):
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
        sorted_array = sorter.sort(array)
        st.success(f"Resultado: {sorted_array}")
    else:
        st.warning("⚠️ Ingresa un array válido para ordenar.")
