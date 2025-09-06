from algoritmos import BubbleSort, MergeSort, SelectionSort, QuickSort
import streamlit as st

st.title("Algoritmos de ordenamiento")

text_array = st.text_input("Ingresa los números separados por comas", "5,4,3,2")

try:
    array = [int(x) for x in text_array.split(",")]
except Exception:
    st.error("Asegúrese de que los números estén separados por comas")
    array = []

algorithm = st.selectbox(
    "Selecciona el método de ordenamiento:",
    ("Bubble Sort", "Merge Sort", "Selection Sort", "Quick Sort"),
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
        sorted_array = sorter.sort(array)
        st.success(f"Resultado: {sorted_array}")
    else:
        st.warning("⚠️ Ingresa un array válido para ordenar.")
