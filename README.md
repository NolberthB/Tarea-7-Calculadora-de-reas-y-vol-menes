# README: Calculadora de Áreas y Volúmenes

## Descripción General

Este proyecto es una calculadora interactiva de áreas y volúmenes de diferentes figuras geométricas. Se desarrolló utilizando Python con el objetivo de poner en práctica conceptos como:

- Uso de funciones para modularizar código.
- Captura de datos desde la consola.
- Implementación de menús interactivos.
- Importación de módulos externos para organizar el proyecto.

La calculadora permite seleccionar entre diferentes figuras geométricas y realizar los cálculos correspondientes para el área y volumen.

---

## Características Principales

1. **Modularidad**: El código está dividido en varios módulos:

   - `calculos_area.py`: Contiene las funciones para calcular áreas de las figuras.
   - `calculos_volumen.py`: Incluye las funciones para calcular volúmenes de las figuras.
   - `menus.py`: Contiene las funciones para mostrar los menús principales y secundarios.

2. **Interactividad**: Los usuarios pueden navegar por los menús y seleccionar las operaciones deseadas ingresando opciones numéricas.

3. **Flexibilidad**: Soporte para una amplia variedad de figuras geométricas.

4. **Uso de Librerías**: Se utiliza `numpy` para los cálculos matemáticos avanzados, como el manejo de π.

---

## Figuras Geométricas Soportadas

### **Cálculo de Áreas**

- Cuadrado
- Triángulo
- Rectángulo
- Círculo
- Esfera
- Cilindro
- Pirámide
- Prisma rectangular

### **Cálculo de Volúmenes**

- Cubo
- Cilindro
- Pirámide
- Prisma rectangular
- Esfera
- Cono

---

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
calculadora_areas_volumenes/
|— utils/
|    |— __init__.py
|    |— calculos_area.py
|    |— calculos_volumen.py
|    |— menus.py
|— main.py
|— README.md
```

### Archivos Principales

1. **`main.py`**:

- Archivo principal que ejecuta el programa.
- Contiene el loop principal y la gestión de menús.

2. **`utils/calculos_area.py`**:

   - Contiene las funciones para calcular áreas de las figuras geométricas.

3. **`utils/calculos_volumen.py`**:

   - Contiene las funciones para calcular volúmenes de las figuras geométricas.

4. **`utils/menus.py`**:

   - Define las funciones para mostrar los menús principales y secundarios.

---

## Ejecución del Programa

### Requisitos Previos

- Python 3.8 o superior.
- Librería `numpy` instalada. Puedes instalarla con:
  ```
  pip install numpy
  ```

### Instrucciones

1. Clona o descarga el repositorio en tu máquina local.
2. Abre una terminal y navega al directorio donde se encuentra el archivo `main.py`.
3. Ejecuta el programa con:
   ```
   python main.py
   ```
4. Sigue las instrucciones en pantalla para seleccionar figuras y realizar cálculos.

---

## Ejemplo de Uso

**Menú Principal:**

```
1. Cálculos de áreas
2. Cálculos de volúmenes
3. Salir
Selecciona una opción:
```

**Submenú de Áreas:**

```
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
```

**Cálculo de Área del Cuadrado:**

```
Ingrese el lado del cuadrado: 5
Área del cuadrado: 25.0
```

---

## Posibles Errores y Soluciones

1. **Error al importar módulos:**

   - Asegúrate de que el directorio `utils` tenga un archivo `__init__.py`.

2. **Error al ingresar valores:**

   - Si ingresas un valor no numérico, el programa lanzará un error. Esto se puede mejorar implementando validaciones.

3. **Cierre del programa inesperado:**

   - Asegúrate de seleccionar opciones válidas en los menús.

---

## Mejoras Futuras

- Implementar validaciones para entradas no válidas.
- Agregar soporte para más figuras geométricas.
- Mejorar la presentación de los resultados con formato.
- Incluir pruebas unitarias para verificar el funcionamiento correcto de las funciones.

---

## Autor

Proyecto desarrollado para una tarea educativa sobre estructuras de código en Python.

NolberthB 

---

## Referencias

Python Software Foundation. (2024). *The Python Standard Library*. Recuperado de https://docs.python.org/3/library/

Repositorio del proyecto: NolberthB. (2024). *Tarea 7: Calculadora de Áreas y Volúmenes*. Recuperado de https://github.com/NolberthB/Tarea-7-Calculadora-de-reas-y-vol-menes

