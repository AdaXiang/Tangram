import cv2
import numpy as np
from piezas import crearPiezasIniciales
from interfaz import pintarTangram, menu, menuTemplates, eleccionTemplate, mostrarPlantilla
from comparador import comprobarPlantilla
from eventos import mouseCallback
from config import ancho_pantalla, alto_pantalla, templates

# Crear piezas
piezas = crearPiezasIniciales()

"""
    Muestra el menú principal y gestiona la selección del modo de juego.
    Retorna:
        - 0 -> seguir en menú
        - 1 -> juego libre
        - 2 -> juego con plantillas
        - -1 -> salir del programa
"""
def seleccionMenu(img, piezas_ref):
    menu(img)
    tecla = cv2.waitKey(20) & 0xFF

    if tecla == ord('1'):
        piezas_ref["lista"] = crearPiezasIniciales()
        return 1
    elif tecla == ord('2'):
        piezas_ref["lista"] = crearPiezasIniciales()
        return 2
    elif tecla == ord('q'):
        return -1
    return 0

"""
    Modo libre: el jugador puede mover y rotar las piezas libremente.
"""
def juegoLibre(piezas_ref):
    while True:
        img = np.ones((alto_pantalla, ancho_pantalla, 3), np.uint8) * 255
        pintarTangram(img, piezas_ref["lista"], 1)

        tecla = cv2.waitKey(20) & 0xFF
        if tecla == ord('r'):
            piezas_ref["lista"] = crearPiezasIniciales()
        elif tecla == ord('q'):
            break


"""
    Modo con plantilla: el jugador elige una figura y debe reproducirla.
"""
def juegoFiguras(piezas_ref, img):
    menuTemplates(img)
    nombreTemplate = eleccionTemplate(templates)
    if nombreTemplate == 0:
        return  # volver al menú 

    imgTemplate = cv2.imread(f"./templates/{nombreTemplate}.png", 1)
    if imgTemplate is None:
        print(f"Error: no se pudo cargar la plantilla {nombreTemplate}")
        return

    while True:
        img = np.ones((alto_pantalla, ancho_pantalla, 3), np.uint8) * 255
        pintarTangram(img, piezas_ref["lista"], 2)

        # Mostrar plantilla guía
        mostrarPlantilla(img, imgTemplate, escala=0.25, margen=20, desplazamiento_y=-30)

        cv2.imshow("Tangram interactivo", img)
        tecla = cv2.waitKey(20) & 0xFF

        if tecla == ord('r'):
            piezas_ref["lista"] = crearPiezasIniciales()
        elif tecla == ord('c'):
            comprobarPlantilla(img, nombreTemplate)
        elif tecla == ord('q'):
            break

#-----------------------------------------------------------------------------------------------

def main():
    cv2.namedWindow("Tangram interactivo")
    piezas_ref = {"lista": crearPiezasIniciales()}
    cv2.setMouseCallback("Tangram interactivo", mouseCallback, piezas_ref)

    while True:
        img = np.ones((alto_pantalla, ancho_pantalla, 3), np.uint8) * 255
        modo = seleccionMenu(img, piezas_ref)

        if modo == -1:  # salir
            break
        elif modo == 1:
            juegoLibre(piezas_ref)
        elif modo == 2:
            juegoFiguras(piezas_ref, img)
            
    cv2.destroyAllWindows()

#-----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
