import cv2
import numpy as np
import tkinter as tk
from config import ancho_pantalla, alto_pantalla

#Listas menús:
menuPrincipal = [
        "TANGRAM",
        "1: Juego libre",
        "2: Juego figuras",
        "q: Salir"
    ]

menuTemplaes = [
        "Plantillas:",
        "1: Conejo",
        "2: Cisne",
        "3: Cohete",
        "q: Salir"
    ]

"""
    Muestra varias líneas de texto centradas en la imagen usando OpenCV.

    Parámetros:
    - img: imagen donde se dibuja el texto 
    - lineas: lista de cadenas (una por línea)
    - tam_fuente: tamaño de la fuente (float)
    - grosor: grosor del texto (int)
    - color: color BGR del texto (tupla)
    - separacion: píxeles entre líneas (int)
"""
def mostrarTextoCentrado(img, lineas, tamFuente, grosor, color, separacion):
    
    fuente = cv2.FONT_HERSHEY_SIMPLEX
    alto_img, ancho_img = img.shape[:2]

    # Calcular posición vertical inicial (centrar bloque de texto)
    y_inicio = (alto_img // 2) - (len(lineas) * separacion // 2)

    for i, texto in enumerate(lineas):
        # Obtener tamaño del texto
        (ancho_texto, alto_texto), _ = cv2.getTextSize(texto, fuente, tamFuente, grosor)
        x = (ancho_img - ancho_texto) // 2  # Centrado horizontal
        y = y_inicio + i * separacion

        # Dibujar texto en la imagen
        cv2.putText(img, texto, (x, y), fuente, tamFuente, color, grosor, cv2.LINE_AA)

"""
    Dibuja el tangram en la pantalla.

    Parámetros:
    - img:  imagen donde se dibuja el tangram
    - modo: 1 o 2, juego libre o juego figuras, respectivamente (int)
"""
def pintarTangram(img, piezas, modo):
    # Dibujar piezas
    for p in piezas:
        cv2.fillPoly(img, [p["puntos"].astype(np.int32)], p["color"])
        cv2.polylines(img, [p["puntos"].astype(np.int32)], True, (0, 0, 0), 1)
    if modo == 1:
        cv2.putText(img, "Click izquierdo: Mover | Click derecho: Rotar | R: Reiniciar | Q: Salir",
                    (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 50), 2)
    elif modo == 2: 
        cv2.putText(img, "Click izquierdo: Mover | Click derecho: Rotar | R: Reiniciar | C: Comprobar | Q: Salir ",
                    (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 50), 2)
    
    cv2.imshow("Tangram interactivo", img)

"""
    Muestra varias líneas de texto centradas en la imagen usando OpenCV.

    Parámetros:
    - img: imagen donde se dibuja el menu
"""
def menu(img):
    img = np.ones((alto_pantalla, ancho_pantalla, 3), np.uint8) * 255
    # Fuente y parámetros
    tamFuente = 3
    grosor = 5
    color = (50, 50, 50)
    separacion = 120

    mostrarTextoCentrado(img, menuPrincipal, tamFuente, grosor, color, separacion)
    cv2.imshow("Tangram interactivo", img)

"""
    Muestra varias líneas de texto centradas en la imagen usando OpenCV.

    Parámetros:
    - img: imagen donde se dibuja el menu
"""
def menuTemplates(img):
    tamFuente = 2
    grosor = 3
    color = (50, 50, 50)
    separacion = 100

    mostrarTextoCentrado(img, menuTemplaes, tamFuente, grosor, color, separacion)
    cv2.imshow("Tangram interactivo", img)

"""
    Devuelve el nombre del template elegido.
"""
def eleccionTemplate(templates):
    tecla = cv2.waitKey(0) & 0xFF # Interacción con las teclas

    if tecla == ord('q'): # Salir
        return 0
    elif tecla == ord('1'):  
        return templates[0]
    elif tecla == ord('2'):
        return templates[1]
    elif tecla == ord('3'):
        return templates[2]
    else:
        return 0  
    
"""
    Dibuja una plantilla reducida en la esquina inferior derecha de la imagen.

    Parámetros:
        - img: imagen base (numpy array)
        - imgTemplate: plantilla original (numpy array)
        - escala: proporción del ancho de la pantalla (float)
        - margen: espacio desde los bordes derecho e inferior (int)
        - desplazamiento_y: ajuste vertical adicional (int)
"""
def mostrarPlantilla(img, imgTemplate, escala=0.25, margen=20, desplazamiento_y=0):   
    alto, ancho = imgTemplate.shape[:2]
    nuevo_ancho = int(img.shape[1] * escala)
    nuevo_alto = int(alto * (nuevo_ancho / ancho))
    template_resized = cv2.resize(imgTemplate, (nuevo_ancho, nuevo_alto))

    x_offset = img.shape[1] - nuevo_ancho - margen
    y_offset = img.shape[0] - nuevo_alto - margen + desplazamiento_y

    roi = img[y_offset:y_offset+nuevo_alto, x_offset:x_offset+nuevo_ancho]
    mezcla = cv2.addWeighted(roi, 0.8, template_resized, 0.5, 0)
    img[y_offset:y_offset+nuevo_alto, x_offset:x_offset+nuevo_ancho] = mezcla