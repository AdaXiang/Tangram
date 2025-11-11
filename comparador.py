import cv2
import numpy as np

"""
    Comprueba si la figura realizada es correcta, es decir, si es igual a la pantilla.

    Parámetros:
    - img:  imagen donde se dibuja el tangram
    - template: nombre de la plantilla con la que se quiere comparar la imagen
"""
def comprobarPlantilla(img, template):
    # Cargar imágenes en blanco y negro
    escena = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plantilla = cv2.imread("templates/"+template+".png", 0)

    # Binarizar (convertir a blanco y negro)
    _, th1 = cv2.threshold(escena, 200, 255, cv2.THRESH_BINARY_INV)
    _, th2 = cv2.threshold(plantilla, 127, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((5, 5), np.uint8)  # Cuanto más grande, más se cierran los huecos
    th1 = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)
    
    # cv2.imshow("Tangram interactivo", th1)
    # cv2.waitKey(2000)  
    # Encontrar contornos
    contours1, _ = cv2.findContours(th1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Tomar el contorno más grande (la figura principal)
    c1 = max(contours1, key=cv2.contourArea)
    c2 = max(contours2, key=cv2.contourArea)

    # Comparar las formas
    similarity = cv2.matchShapes(c1, c2, cv2.CONTOURS_MATCH_I1, 0.0)
    print(f"similarity: {similarity:.4f}")
    if similarity < 0.3:
        texto = "La figura coincide"
        color = (0, 200, 0)
    else:
        texto = "La figura no coincide"
        color = (0, 0, 255)

    # Copia temporal de la imagen para mostrar mensaje
    img_resultado = img.copy()
    (ancho_texto, alto_texto,), baseline = cv2.getTextSize(texto, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)
    alto_imagen, ancho_imagen, canales = img.shape
    posicion_x = int((ancho_imagen - ancho_texto) / 2)
    posicion_y = int(alto_imagen / 2 + alto_texto / 2)
    margen = 10
    x1, y1 = posicion_x - margen, posicion_y - alto_texto - margen
    x2, y2 = posicion_x + ancho_texto  + margen, posicion_y + baseline + margen
    # Dibujar mensaje 
    cv2.rectangle(img_resultado, (x1, y1), (x2, y2), (225, 225, 225), thickness=-1)
    cv2.rectangle(img_resultado, (x1, y1), (x2, y2), (211, 211, 211), thickness=2)
    cv2.putText(img_resultado, texto, (posicion_x, posicion_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3, cv2.LINE_AA)

    # Mostrar imagen con mensaje durante 3 segundos
    cv2.imshow("Tangram interactivo", img_resultado)
    cv2.waitKey(2000)  