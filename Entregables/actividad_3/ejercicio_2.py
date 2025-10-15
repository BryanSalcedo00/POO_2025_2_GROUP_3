import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from abc import ABC, abstractmethod
import math
import os

# Clases de figuras geométricas
class Figura(ABC):
    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_superficie(self):
        pass

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * self.radio**2 * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4/3) * math.pi * self.radio**3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio**2

class Piramide(Figura):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        return (1/3) * (self.base ** 2) * self.altura

    def calcular_superficie(self):
        base_area = self.base ** 2
        lateral_area = 2 * self.base * self.apotema
        return base_area + lateral_area

class Cubo(Figura):
    def __init__(self, arista):
        self.arista = arista

    def calcular_volumen(self):
        return self.arista ** 3

    def calcular_superficie(self):
        return 6 * (self.arista ** 2)

class Prisma(Figura):
    def __init__(self, base, altura, profundidad):
        self.base = base  # longitud de la base del triángulo
        self.altura = altura  # altura del triángulo base
        self.profundidad = profundidad  # profundidad del prisma

    def calcular_volumen(self):
        area_base = (self.base * self.altura) / 2  # triángulo
        return area_base * self.profundidad

    def calcular_superficie(self):
        area_base = (self.base * self.altura) / 2
        perimetro_base = self.base + 2 * math.sqrt((self.base / 2) ** 2 + self.altura ** 2)  # isósceles
        area_lateral = perimetro_base * self.profundidad
        return 2 * area_base + area_lateral


# App con interfaz gráfica
class FiguraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geométricas")

        self.figura_var = tk.StringVar()
        self.figura_var.set("Cilindro")

        # Combobox para seleccionar figura
        tk.Label(root, text="Selecciona la figura:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        opciones = ["Cilindro", "Esfera", "Pirámide", "Cubo", "Prisma"]
        self.combo_figura = ttk.Combobox(root, textvariable=self.figura_var, values=opciones, state="readonly")
        self.combo_figura.grid(row=0, column=1, padx=10, pady=5)
        self.combo_figura.bind("<<ComboboxSelected>>", self.actualizar_campos)

        # Frame para inputs dinámicos
        self.frame_inputs = tk.Frame(root)
        self.frame_inputs.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Frame para imagen
        self.frame_imagen = tk.Frame(root)
        self.frame_imagen.grid(row=1, column=2, padx=10, pady=10)

        # Botón calcular
        self.btn_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=2, column=0, columnspan=3, pady=10)

        # Resultado
        self.resultado = tk.Label(root, text="", justify="left")
        self.resultado.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.campos = {}  # Para entradas
        self.imagen_label = None
        self.imagen_actual = None  # Referencia para evitar GC

        self.actualizar_campos()

    def actualizar_campos(self, event=None):
        # Limpiar widgets inputs
        for widget in self.frame_inputs.winfo_children():
            widget.destroy()

        # Limpiar imagen
        for widget in self.frame_imagen.winfo_children():
            widget.destroy()

        self.campos.clear()
        figura = self.figura_var.get()

        # Crear campos segun figura
        if figura == "Cilindro":
            self.crear_campo("Radio (cm):", "radio")
            self.crear_campo("Altura (cm):", "altura")
        elif figura == "Esfera":
            self.crear_campo("Radio (cm):", "radio")
        elif figura == "Pirámide":
            self.crear_campo("Base (cm):", "base")
            self.crear_campo("Altura (cm):", "altura")
            self.crear_campo("Apotema (cm):", "apotema")
        elif figura == "Cubo":
            self.crear_campo("Arista (cm):", "arista")
        elif figura == "Prisma":
            self.crear_campo("Base (cm):", "base")
            self.crear_campo("Altura Base (cm):", "altura")
            self.crear_campo("Profundidad (cm):", "profundidad")

        self.mostrar_imagen(figura)

    def crear_campo(self, texto, key):
        label = tk.Label(self.frame_inputs, text=texto)
        label.pack(anchor="w")
        entry = tk.Entry(self.frame_inputs)
        entry.pack(fill="x", pady=2)
        self.campos[key] = entry

    def mostrar_imagen(self, figura):
        carpeta_imagenes = "imagenes_figuras"
        nombre_archivo = figura.lower() + ".png"

        ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)

        if os.path.exists(ruta_imagen):
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((150, 150), Image.Resampling.LANCZOS)
            self.imagen_actual = ImageTk.PhotoImage(imagen)
            self.imagen_label = tk.Label(self.frame_imagen, image=self.imagen_actual)
            self.imagen_label.pack()
        else:
            # Si no hay imagen, mostramos texto
            self.imagen_label = tk.Label(self.frame_imagen, text=f"No hay imagen para {figura}")
            self.imagen_label.pack()

    def calcular(self):
        figura = self.figura_var.get()
        try:
            if figura == "Cilindro":
                radio = float(self.campos["radio"].get())
                altura = float(self.campos["altura"].get())
                figura_obj = Cilindro(radio, altura)
            elif figura == "Esfera":
                radio = float(self.campos["radio"].get())
                figura_obj = Esfera(radio)
            elif figura == "Pirámide":
                base = float(self.campos["base"].get())
                altura = float(self.campos["altura"].get())
                apotema = float(self.campos["apotema"].get())
                figura_obj = Piramide(base, altura, apotema)
            elif figura == "Cubo":
                arista = float(self.campos["arista"].get())
                figura_obj = Cubo(arista)
            elif figura == "Prisma":
                base = float(self.campos["base"].get())
                altura = float(self.campos["altura"].get())
                profundidad = float(self.campos["profundidad"].get())
                figura_obj = Prisma(base, altura, profundidad)
            else:
                messagebox.showerror("Error", "Figura no reconocida.")
                return
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
            return

        volumen = figura_obj.calcular_volumen()
        superficie = figura_obj.calcular_superficie()

        texto_resultado = (
            f"Volumen: {volumen:.2f} cm³\n"
            f"Superficie: {superficie:.2f} cm²"
        )

        self.resultado.config(text=texto_resultado)


# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = FiguraApp(root)
    root.mainloop()