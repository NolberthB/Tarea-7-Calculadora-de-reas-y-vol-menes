import numpy as np

# Funciones para calcular el volumen de figuras geometricas.
def volumen_cubo(lado):
    return lado ** 3

def voluen_cilindro(radio, altura):
    return np.pi * radio ** 2 * altura

def volumen_piramide(ancho, longitud, altura):
    return (1/3) * ancho * longitud * altura

def volumen_prisma_rectangular(ancho, longitud, altura):
    return ancho * longitud * altura

def volumen_esfera(radio):
    return (4/3) * np.pi * radio ** 3

def volumen_cono(radio, altura):
    return (1/3) * np.pi * radio ** 2 * altura