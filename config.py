import tkinter as tk

# Obtener tamaño de pantalla
root = tk.Tk()
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
root.destroy()

# Plantillas para jugar a hacer figuras con guía
templates = ["conejo", "cisne", "cohete"]