# Algoritmos de Ordenamiento y Estrategias de Resolución

Este proyecto implementa algoritmos clásicos de ordenamiento, backtracking y algoritmos voraces en Python, con una arquitectura orientada a objetos y una interfaz gráfica sencilla usando Streamlit.

---

## Estructura del Proyecto

```
algoritmos/
│
├── ordenamiento/
│   ├── base.py
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── selection_sort.py
│   └── busqueda_binaria.py
│
├── backtracking/
│   ├── salto_caballo.py
│   ├── torres_hanoi.py
│   └── utils/
│       └── ajedrez.py
│
├── voraces/
│   ├── agente_viajero.py
│   ├── cambio_moneda.py
│   ├── Dijkstra.py
│   └── Kruskal.py
│
└── __init__.py
main.py
streamlit_pages/
│   ├── __init__.py
│   ├── ordenamiento.py
│   ├── backtracking.py
│   └── voraces.py
```

- **algoritmos/ordenamiento/**: Implementaciones de algoritmos de ordenamiento y búsqueda.
- **algoritmos/backtracking/**: Problemas clásicos resueltos con backtracking y utilidades.
- **algoritmos/voraces/**: Algoritmos voraces clásicos.
- **main.py**: Interfaz gráfica principal con Streamlit.
- **streamlit_pages/**: Páginas modulares para la interfaz Streamlit.

---

## Instalación

1. **Clona el repositorio** (o descarga los archivos):

   ```sh
   git clone <URL-del-repositorio>
   cd "Algoritmos de ordenamiento"
   ```

2. **Crea un entorno virtual** (opcional pero recomendado):

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias**:

   ```sh
   pip install -r requirements.txt
   ```

   O si usas `pyproject.toml`:

   ```sh
   pip install .
   ```

   O directamente:

   ```sh
   pip install streamlit numpy pandas matplotlib networkx
   ```

---

## Uso desde main.py (Interfaz Streamlit)

La aplicación permite al usuario:
- Ingresar una lista de números separados por comas.
- Seleccionar el algoritmo de ordenamiento (Bubble Sort, Merge Sort, Selection Sort, Quick Sort, Insertion Sort).
- Visualizar el resultado ordenado y el tiempo de ejecución.
- Generar arrays aleatorios de tamaño 1, 100 o 1000.
- Navegar entre páginas de algoritmos de ordenamiento, backtracking y voraces.
- Visualizar logs de ejecución en el panel lateral.

### Ejecución

Desde la terminal, ejecuta:

```sh
streamlit run main.py
```

Esto abrirá la interfaz web en tu navegador.

### Ejemplo de uso en la interfaz

1. Ingresa: `5,4,3,2`
2. Selecciona el algoritmo deseado.
3. Haz clic en **Ordenar**.
4. El resultado y el tiempo de ejecución aparecerán en pantalla.
5. Puedes generar arrays aleatorios y ver logs en el sidebar.

---

## Uso como módulo Python

También puedes importar y usar los algoritmos directamente en tus scripts:

```python
from algoritmos.ordenamiento.bubble_sort import BubbleSort
from algoritmos.ordenamiento.merge_sort import MergeSort

bs = BubbleSort()
resultado_bs = bs.sort([5, 3, 8, 1])
print("BubbleSort:", resultado_bs, "Tiempo:", bs.execution_time)

ms = MergeSort()
resultado_ms = ms.sort([5, 3, 8, 1])
print("MergeSort:", resultado_ms, "Tiempo:", ms.execution_time)
```

---

## Decorador timer_decorator

El decorador `timer_decorator` mide el tiempo de ejecución de los métodos de ordenamiento y almacena el resultado en el atributo `execution_time` de la instancia.

---

## Requisitos

- Python 3.7 o superior
- [Streamlit](https://streamlit.io/)
- numpy, pandas, matplotlib, networkx

---

## Créditos

Grupo 3 de Algoritmos  
UPN - 2025