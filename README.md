# Tarea 7: Calculadora de áreas y volúmenes
Fin de aprendizaje: Implementa un código en Python para determinar el área y volumen de diferentes figuras geométricas, con el fin de aplicar funciones para estructurar mejor tu programa y poner en práctica el uso de operadores aritméticos.

Descripción General

Este proyecto es una calculadora interactiva de áreas y volúmenes de diferentes figuras geométricas. Se desarrolló utilizando Python con el objetivo de poner en práctica conceptos como:

Uso de funciones para modularizar código.

Captura de datos desde la consola.

Implementación de menús interactivos.

Importación de módulos externos para organizar el proyecto.

La calculadora permite seleccionar entre diferentes figuras geométricas y realizar los cálculos correspondientes para el área y volumen.

Características Principales

Modularidad: El código está dividido en varios módulos:

calculos_area.py: Contiene las funciones para calcular áreas de las figuras.

calculos_volumen.py: Incluye las funciones para calcular volúmenes de las figuras.

menus.py: Contiene las funciones para mostrar los menús principales y secundarios.

Interactividad: Los usuarios pueden navegar por los menús y seleccionar las operaciones deseadas ingresando opciones numéricas.

Flexibilidad: Soporte para una amplia variedad de figuras geométricas.

Uso de Librerías: Se utiliza numpy para los cálculos matemáticos avanzados, como el manejo de π.

Figuras Geométricas Soportadas

Cálculo de Áreas

Cuadrado

Triángulo

Rectángulo

Círculo

Esfera

Cilindro

Pirámide

Prisma rectangular

Cálculo de Volúmenes

Cubo

Cilindro

Pirámide

Prisma rectangular

Esfera

Cono

Estructura del Proyecto

La estructura del proyecto es la siguiente:

calculadora_areas_volumenes/
|— utils/
|    |— __init__.py
|    |— calculos_area.py
|    |— calculos_volumen.py
|    |— menus.py
|— main.py
|— README.md

Archivos Principales

main.py:

Archivo principal que ejecuta el programa.

Contiene el loop principal y la gestión de menús.

utils/calculos_area.py:

Contiene las funciones para calcular áreas de las figuras geométricas.

utils/calculos_volumen.py:

Contiene las funciones para calcular volúmenes de las figuras geométricas.

utils/menus.py:

Define las funciones para mostrar los menús principales y secundarios.

Ejecución del Programa

Requisitos Previos

Python 3.8 o superior.

Librería numpy instalada. Puedes instalarla con:

pip install numpy

Instrucciones

Clona o descarga el repositorio en tu máquina local.

Abre una terminal y navega al directorio donde se encuentra el archivo main.py.

Ejecuta el programa con:

python main.py

Sigue las instrucciones en pantalla para seleccionar figuras y realizar cálculos.

Ejemplo de Uso

Menú Principal:

1. Cálculos de áreas
2. Cálculos de volúmenes
3. Salir
Selecciona una opción:

Submenú de Áreas:

1. Cuadrado
2. Triángulo
3. Rectángulo
4. Círculo
5. Esfera
6. Cilindro
7. Pirámide
8. Prisma rectangular
0. Volver al menú principal
Selecciona una opción:

Cálculo de Área del Cuadrado:

Ingrese el lado del cuadrado: 5
Área del cuadrado: 25.0

Posibles Errores y Soluciones

Error al importar módulos:

Asegúrate de que el directorio utils tenga un archivo __init__.py.

Error al ingresar valores:

Si ingresas un valor no numérico, el programa lanzará un error. Esto se puede mejorar implementando validaciones.

Cierre del programa inesperado:

Asegúrate de seleccionar opciones válidas en los menús.
