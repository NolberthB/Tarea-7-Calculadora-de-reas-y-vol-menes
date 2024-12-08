import numpy as np

# Funciones de calculo de areas
def area_cuadrado(lado): 
    return lado ** 2

def area_triangulo(base, altura): 
    return 0.5 * base * altura

def area_rectangulo(longitud, ancho):
    return longitud * ancho

def area_circulo(radio):
    return np.pi * radio ** 2

def area_esfera(radio):
    return 4 * np.pi * radio ** 2

def area_cilindro(radio, altura):
    return 2 * np.pi * radio * (radio + altura)

def area_piramide(ancho, longitud, altura):
    base_area = ancho * longitud
    slant_height = np.sqrt((ancho / 2) ** 2 + altura ** 2)
    side_area = longitud * slant_height
    return base_area + 2 * side_area

def area_prisma_rectangular(ancho, longitud, altura):
    return 2 * (ancho * longitud + ancho * altura + longitud * altura)
