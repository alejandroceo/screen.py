import tkinter as tk
from tkinter import filedialog
import pyautogui
import os

class CapturaPantallaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Captura de Pantalla")

        # Crear widgets
        self.label = tk.Label(root, text="Presiona el botón para tomar una captura de pantalla")
        self.boton_capturar = tk.Button(root, text="Capturar", command=self.tomar_screenshot)
        self.boton_salir = tk.Button(root, text="Salir", command=self.salir)

        # Organizar widgets en la interfaz
        self.label.pack(pady=10)
        self.boton_capturar.pack(pady=5)
        self.boton_salir.pack(pady=5)

    def tomar_screenshot(self):
        # Tomar la captura de pantalla de toda la pantalla
        screenshot = pyautogui.screenshot()

        # Mostrar el cuadro de diálogo para guardar la captura de pantalla
        ruta_guardado = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", "*.png"), ("Todos los archivos", "*.*")])

        if ruta_guardado:
            screenshot.save(ruta_guardado)
            print(f"Captura de pantalla guardada como {ruta_guardado}")

    def salir(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CapturaPantallaApp(root)
    root.mainloop()
