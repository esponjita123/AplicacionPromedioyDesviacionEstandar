# Proyecto de Calculadora en Python

## Descripción del Proyecto

Este proyecto consiste en una calculadora para calcular el promedio y la desviación estándar de una lista de números. Está implementado en Python y contiene una estructura con carpetas para el código fuente y las pruebas unitarias. También cuenta con manejo de excepciones personalizadas.

## Estructura del Proyecto

El proyecto está organizado en dos carpetas principales:

- **src**: Contiene el código fuente de la calculadora.
- **tests**: Contiene las pruebas unitarias y excepciones personalizadas.

### Archivos en la carpeta src:

- **calculadora.py**: Este archivo contiene las funciones principales de la calculadora:
  - `calcular_promedio(elementos)`: Calcula el promedio de una lista de números. Si la lista está vacía, lanza una excepción personalizada `NoSePuedeCalcular`. Si algún elemento de la lista no es numérico, lanza un `TypeError`.
  - `calcular_desviacion_estandar(elementos)`: Calcula la desviación estándar de una lista de números. También maneja excepciones similares a las de la función de promedio.
  
- **main.py**: Es el archivo de entrada principal del programa. Proporciona una interfaz interactiva en la que el usuario puede ingresar números hasta que decida detenerse. Luego, calcula y muestra el promedio y la desviación estándar usando las funciones definidas en `calculadora.py`. Maneja excepciones para listas vacías y tipos de datos no numéricos.

### Archivos en la carpeta tests:

- **excepcion.py**: Este archivo define la excepción personalizada `NoSePuedeCalcular`, la cual es utilizada en las funciones de `calculadora.py` para indicar cuándo no es posible realizar los cálculos (por ejemplo, cuando la lista está vacía).

- **test_calculadora.py**: Contiene pruebas unitarias utilizando el módulo `unittest`. Las pruebas aseguran que las funciones de la calculadora (promedio y desviación estándar) se comporten correctamente en diferentes escenarios:
  - Listas vacías.
  - Listas con un solo elemento.
  - Listas con múltiples elementos.
  - Manejo de datos no numéricos.

