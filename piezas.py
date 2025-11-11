import numpy as np
import math

#-----------------------------------------------------------------------------------------------

"""
    Crea y devuelve una pieza del tangram con sus propiedades iniciales.

    Parámetros:
    ------------
    - puntos : lista de coordenadas (x, y) que definen los vértices de la pieza en orden.
               Cada punto representa un vértice del polígono que forma la figura (list[tuple[float, float]])
    - color : color de la pieza en formato BGR (Blue, Green, Red) (tuple[int, int, int])
    - nombre : nombre identificativo de la pieza (str)

    Retorna:
    --------
        Un diccionario con las siguientes claves:
        - "nombre": nombre de la pieza (str)
        - "puntos": matriz NumPy (float32) con las coordenadas de los vértices
        - "color": color de la pieza (tuple BGR)
        - "angulo": ángulo actual de rotación en grados (float, inicializado en 0)
    """
def crear_pieza(puntos, color, nombre):
    return {"nombre": nombre, "puntos": np.array(puntos, dtype=np.float32), "color": color, "angulo": 0}

#-----------------------------------------------------------------------------------------------

"""
    Rota una pieza del tangram un número determinado de grados alrededor de su centro geométrico.

    Parámetros:
    ------------
    pieza: diccionario que representa la pieza a rotar. Debe contener:
            - "puntos": matriz NumPy (n, 2) con las coordenadas (x, y) de sus vértices.
            - "angulo": valor actual de rotación (no se usa directamente pero puede ser actualizado externamente).

    grados: ángulo de rotación en grados. Un valor positivo rota la pieza en sentido antihorario (float)

    Descripción:
    -------------
    - Calcula el centroide (centro geométrico) de la pieza.
    - Convierte los grados a radianes.
    - Construye la matriz de rotación 2D.
    - Aplica la rotación a todos los vértices de la pieza manteniendo su posición relativa al centro.
    """
def rotar_pieza(pieza, grados):
    centro = np.mean(pieza["puntos"], axis=0)
    rad = math.radians(grados)
    R = np.array([[math.cos(rad), -math.sin(rad)],
                  [math.sin(rad),  math.cos(rad)]])
    pieza["puntos"] = np.dot(pieza["puntos"] - centro, R.T) + centro

#-----------------------------------------------------------------------------------------------
# Crear piezas inicales del tangram con un offsetInicial
offsetIni = 100
"""
    Devuelve una lista de figuras que forman un cuadrado de 200x200 pixeles.
"""
def crearPiezasIniciales(): 
    return [
        # Triángulo grande 1
        crear_pieza([(0+offsetIni, 0+offsetIni), (100+offsetIni, 100+offsetIni), (0+offsetIni, 200+offsetIni)], (0, 0, 255), "Triángulo grande 1"),
        # Triángulo grande 2
        crear_pieza([(0+offsetIni, 0+offsetIni), (100+offsetIni, 100+offsetIni), (200+offsetIni, 0+offsetIni)], (0, 255, 0), "Triángulo grande 2"),
        # Triángulo mediano
        crear_pieza([(200+offsetIni, 100+offsetIni), (200+offsetIni, 200+offsetIni), (100+offsetIni, 200+offsetIni)], (255, 0, 0), "Triángulo mediano"),
        # Triángulo pequeño 1
        crear_pieza([(200+offsetIni, 0+offsetIni), (200+offsetIni, 100+offsetIni), (150+offsetIni, 50+offsetIni)], (221, 156, 0), "Triángulo pequeño 1"),
        # Triángulo pequeño 2
        crear_pieza([(100+offsetIni, 100+offsetIni), (150+offsetIni, 150+offsetIni), (50+offsetIni, 150+offsetIni)], (255, 0, 255), "Triángulo pequeño 2"),
        # Cuadrado
        crear_pieza([(100+offsetIni, 100+offsetIni), (150+offsetIni, 50+offsetIni), (200+offsetIni, 100+offsetIni), (150+offsetIni, 150+offsetIni)], (0, 165, 255), "Cuadrado"),
        # Paralelogramo
        crear_pieza([(0+offsetIni, 200+offsetIni), (100+offsetIni, 200+offsetIni), (150+offsetIni, 150+offsetIni), (50+offsetIni, 150+offsetIni)], (128, 0, 128), "Paralelogramo")
]