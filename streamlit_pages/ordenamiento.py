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


st.set_page_config(layout="wide")

def mostrar():
    st.title("Algoritmos de ordenamiento")

    sup_col1, sup_col2 = st.columns([3, 1])
    
    with sup_col1:
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

        # Opción para generar arrays aleatorios
        col1, col2 = st.columns([2, 1])
        with col2:
            size = st.selectbox("Tamaño del array aleatorio", (10, 50, 100))
            if st.button("Generar array aleatorio"):
                array = random.sample(range(1, size+1), k=size)
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
    with sup_col2:
        match algorithm:
            case "Bubble Sort":
                desc = """Bubble Sort

Descripción: Recorre repetidamente la lista, comparando elementos adyacentes e intercambiándolos si están en el orden incorrecto. Es sencillo pero muy ineficiente para listas grandes.

Complejidad:

Peor caso: O(n²)

Mejor caso (lista ya ordenada): O(n)

Promedio: O(n²)"""
            case "Merge Sort":
                desc = """Merge Sort

Descripción: Divide la lista en mitades recursivamente hasta llegar a listas de un solo elemento, luego las combina en orden. Es eficiente y estable.

Complejidad:

Peor caso: O(n log n)

Mejor caso: O(n log n)

Promedio: O(n log n)"""
            case "Selection Sort":
                desc = """Selection Sort

Descripción: Encuentra el elemento mínimo en cada pasada y lo coloca en su posición correcta. Fácil de entender, pero poco eficiente.

Complejidad:

Peor caso: O(n²)

Mejor caso: O(n²)

Promedio: O(n²)"""
            case "Quick Sort":
                desc = """Quick Sort

Descripción: Escoge un elemento como pivote, divide la lista en elementos menores y mayores que él, y aplica recursión. Es muy rápido en promedio, pero depende de la elección del pivote.

Complejidad:

Peor caso: O(n²) (si los pivotes son malos)

Mejor caso: O(n log n)

Promedio: O(n log n)"""
            case "Insertion Sort":
                desc = """Insertion Sort

Descripción: Construye la lista ordenada de izquierda a derecha, insertando cada nuevo elemento en la posición correcta. Es útil en listas pequeñas o casi ordenadas.

Complejidad:

Peor caso: O(n²)

Mejor caso (lista ya ordenada): O(n)

Promedio: O(n²)"""
            case "Busqueda Binaria":
                desc = """Binary Search

Descripción: Busca un elemento en una lista ordenada dividiéndola repetidamente a la mitad. Muy eficiente comparado con la búsqueda secuencial.

Complejidad:

Peor caso: O(log n)

Mejor caso: O(1)

Promedio: O(log n)"""
            case _:
                desc = 'missing'
        st.text_area(label='Algorithm Description', value=desc, height='content')
                

    ##para busqueda binaria pedimos lo que se va a ejecutar



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
