# Algoritmos de Ordenamiento

Este proyecto implementa algoritmos clásicos de ordenamiento en Python, con una arquitectura orientada a objetos y una interfaz gráfica sencilla usando Streamlit.

## Estructura del Proyecto

```
algoritmos/
│
├── __init__.py
├── base.py
├── bubble_sort.py
├── merge_sort.py
└── __pycache__/
main.py
```

- **algoritmos/**: Paquete que contiene las implementaciones de los algoritmos y la clase base.
  - `base.py`: Clase base `AlgoritmoBase` con utilidades y decorador para medir tiempo de ejecución.
  - `bubble_sort.py`: Implementación de Bubble Sort.
  - `merge_sort.py`: Implementación de Merge Sort.
- **main.py**: Interfaz gráfica con Streamlit para probar los algoritmos.

## Uso desde main.py (Interfaz Streamlit)

La aplicación permite al usuario:
- Ingresar una lista de números separados por comas.
- Seleccionar el algoritmo de ordenamiento (Bubble Sort o Merge Sort).
- Visualizar el resultado ordenado.


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
   pip install streamlit numpy pandas
   ```
   
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
4. El resultado aparecerá en pantalla.

## Uso como módulo Python

También puedes importar y usar los algoritmos directamente en tus scripts:

```python
from algoritmos.bubble_sort import BubbleSort
from algoritmos.merge_sort import MergeSort

bs = BubbleSort()
resultado_bs = bs.sort([5, 3, 8, 1])
print("BubbleSort:", resultado_bs, "Tiempo:", bs.execution_time)

ms = MergeSort()
resultado_ms = ms.sort([5, 3, 8, 1])
print("MergeSort:", resultado_ms, "Tiempo:", ms.execution_time)
```

## Decorador timer_decorator

El decorador `timer_decorator` mide el tiempo de ejecución de los métodos de ordenamiento y almacena el resultado en el atributo `execution_time` de la instancia.

## Requisitos

- Python 3.7 o superior
- [Streamlit](https://streamlit.io/) (`pip install streamlit`)

## Créditos

Grupo 3 de Algoritmos