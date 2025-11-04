import cv2
import numpy as np
from piezas import rotar_pieza

pieza_activa = None
arrastrando = False
offset = np.array([0, 0], dtype=np.float32)

"""
    Interacción con el ratón.

    Parámetros:
    - event: int  
        Tipo de evento del ratón detectado por OpenCV (por ejemplo, clic, movimiento, etc.).  
        Puede tomar valores como:
            - cv2.EVENT_LBUTTONDOWN: clic izquierdo presionado  
            - cv2.EVENT_LBUTTONUP: clic izquierdo liberado  
            - cv2.EVENT_MOUSEMOVE: movimiento del ratón  
            - cv2.EVENT_RBUTTONDOWN: clic derecho presionado  

    - x: coordenada horizontal (en píxeles) del puntero del ratón dentro de la ventana (int)
    - y: coordenada vertical (en píxeles) del puntero del ratón dentro de la ventana (int)
    - flags: indicadores adicionales sobre el estado del ratón o teclado. En este caso no se utiliza.
    - param: parámetro adicional que puede pasarse al configurar el callback con `cv2.setMouseCallback()`.  
             No se usa en esta implementación (any)
"""
def mouseCallback(event, x, y, flags, param):
    global pieza_activa, arrastrando, offset
    piezas = param["lista"]

    if event == cv2.EVENT_LBUTTONDOWN:
        # Ver qué pieza se tocó (revisar de arriba a abajo)
        for p in reversed(piezas):
            if cv2.pointPolygonTest(p["puntos"].astype(np.int32), (x, y), False) >= 0:
                pieza_activa = p
                arrastrando = True
                offset = np.array([x, y]) - np.mean(p["puntos"], axis=0)
                break

    elif event == cv2.EVENT_MOUSEMOVE and arrastrando and pieza_activa is not None:
        centro_actual = np.mean(pieza_activa["puntos"], axis=0)
        desplazamiento = np.array([x, y]) - offset - centro_actual
        pieza_activa["puntos"] += desplazamiento

    elif event == cv2.EVENT_LBUTTONUP:
        arrastrando = False

    elif event == cv2.EVENT_RBUTTONDOWN and pieza_activa is not None:
        rotar_pieza(pieza_activa, 15)