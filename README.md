# Tangram

## Introducción

El **Tangram** es un rompecabezas tradicional de origen chino que consta de siete piezas, conocidas como "tans". Estas piezas son combinadas para formar una figura específica. El objetivo del juego es usar todas las piezas para crear una forma o figura sin superponer ninguna pieza. Es un juego que promueve la agilidad mental, la creatividad y la resolución de problemas.

En este proyecto, implementamos un enfoque que puede incluir tanto la visualización como la resolución de problemas usando la biblioteca OpenCV.

### Modos de Juego

El proyecto incluye dos modos de juego:

1. **Modo Normal**:  
   El jugador debe formar una figura específica utilizando las piezas del Tangram, sin tener una referencia visual de la forma final. El objetivo es crear la figura correctamente utilizando todas las piezas.

2. **Modo Copiar Figura**:  
   En este modo, el jugador debe copiar una figura que se muestra como plantilla. Una vez que se coloca todas las piezas, el sistema verifica si la figura está correctamente formada comparándola con la plantilla. Este modo permite comprobar si la figura fue realizada correctamente o no.

## Instalación

### Requisitos

Antes de ejecutar este proyecto, asegúrate de tener las siguientes herramientas instaladas:

1. **Python 3**  
   Puedes descargar Python desde su página oficial [python.org](https://www.python.org/downloads/).

2. **OpenCV**  
   Para instalar OpenCV en tu entorno de Python, usa el siguiente comando:

   ```bash
   pip install opencv-python

