import tkinter as tk
from tkinter import messagebox
import re

class Programador:
    """Clase que representa un programador."""
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.validar_nombre_apellido()

    def validar_nombre_apellido(self):
        if not self.nombre.isalpha() or not self.apellidos.isalpha():
            raise ValueError("Nombre y apellidos deben contener solo letras.")
        if len(self.nombre) >= 20 or len(self.apellidos) >= 20:
            raise ValueError("Nombre o apellidos no pueden tener 20 o más caracteres.")


class EquipoMaraton:
    """Clase que representa un equipo de maratón."""
    def __init__(self, nombre_equipo, universidad, lenguaje, tamano_equipo):
        if tamano_equipo < 2 or tamano_equipo > 3:
            raise ValueError("El tamaño del equipo debe ser 2 o 3.")
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano_equipo = tamano_equipo
        self.programadores = []

    def equipo_completo(self):
        return len(self.programadores) == self.tamano_equipo

    def añadir_programador(self, programador):
        if self.equipo_completo():
            raise ValueError("El equipo ya está completo.")
        self.programadores.append(programador)


class ValidarContrasena:
    """Clase que valida contraseñas según los requisitos."""
    @staticmethod
    def validar_contrasena(contrasena, confirmacion):
        if contrasena != confirmacion:
            raise ValueError("Las contraseñas no coinciden.")
        if len(contrasena) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        if " " in contrasena:
            raise ValueError("La contraseña no debe contener espacios.")
        if not re.search(r"[a-z]", contrasena):
            raise ValueError("La contraseña debe tener al menos una letra minúscula.")
        if not re.search(r"[A-Z]", contrasena):
            raise ValueError("La contraseña debe tener al menos una letra mayúscula.")
        if not re.search(r"[0-9]", contrasena):
            raise ValueError("La contraseña debe tener al menos un número.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena):
            raise ValueError("La contraseña debe tener al menos un carácter especial (!@#$...).")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Equipo Maratón de Programación")

        # Entradas del equipo
        tk.Label(root, text="Nombre del equipo:").grid(row=0, column=0)
        tk.Label(root, text="Universidad:").grid(row=1, column=0)
        tk.Label(root, text="Lenguaje:").grid(row=2, column=0)
        tk.Label(root, text="Tamaño del equipo (2 o 3):").grid(row=3, column=0)

        self.nombre_equipo = tk.Entry(root)
        self.universidad = tk.Entry(root)
        self.lenguaje = tk.Entry(root)
        self.tamano_equipo = tk.Entry(root)

        self.nombre_equipo.grid(row=0, column=1)
        self.universidad.grid(row=1, column=1)
        self.lenguaje.grid(row=2, column=1)
        self.tamano_equipo.grid(row=3, column=1)

        # Entradas de programadores
        tk.Label(root, text="Programador 1 - Nombre:").grid(row=4, column=0)
        tk.Label(root, text="Programador 1 - Apellidos:").grid(row=5, column=0)
        tk.Label(root, text="Programador 2 - Nombre:").grid(row=6, column=0)
        tk.Label(root, text="Programador 2 - Apellidos:").grid(row=7, column=0)
        tk.Label(root, text="Programador 3 - Nombre (opcional):").grid(row=8, column=0)
        tk.Label(root, text="Programador 3 - Apellidos (opcional):").grid(row=9, column=0)

        self.p1_nombre = tk.Entry(root)
        self.p1_apellidos = tk.Entry(root)
        self.p2_nombre = tk.Entry(root)
        self.p2_apellidos = tk.Entry(root)
        self.p3_nombre = tk.Entry(root)
        self.p3_apellidos = tk.Entry(root)

        self.p1_nombre.grid(row=4, column=1)
        self.p1_apellidos.grid(row=5, column=1)
        self.p2_nombre.grid(row=6, column=1)
        self.p2_apellidos.grid(row=7, column=1)
        self.p3_nombre.grid(row=8, column=1)
        self.p3_apellidos.grid(row=9, column=1)

        # Entradas de contraseña
        tk.Label(root, text="Contraseña:").grid(row=10, column=0)
        tk.Label(root, text="Confirmar contraseña:").grid(row=11, column=0)
        self.contrasena = tk.Entry(root, show="*")
        self.confirmacion = tk.Entry(root, show="*")
        self.contrasena.grid(row=10, column=1)
        self.confirmacion.grid(row=11, column=1)

        # Botones
        tk.Button(root, text="Crear Equipo", command=self.crear_equipo).grid(row=12, column=0)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=12, column=1)

    def crear_equipo(self):
        try:
            equipo = EquipoMaraton(
                self.nombre_equipo.get(),
                self.universidad.get(),
                self.lenguaje.get(),
                int(self.tamano_equipo.get())
            )

            # Programadores obligatorios
            p1 = Programador(self.p1_nombre.get(), self.p1_apellidos.get())
            p2 = Programador(self.p2_nombre.get(), self.p2_apellidos.get())
            equipo.añadir_programador(p1)
            equipo.añadir_programador(p2)

            # Programador opcional
            if self.p3_nombre.get() and self.p3_apellidos.get():
                p3 = Programador(self.p3_nombre.get(), self.p3_apellidos.get())
                equipo.añadir_programador(p3)

            # Validar contraseña
            ValidarContrasena.validar_contrasena(
                self.contrasena.get(), self.confirmacion.get()
            )

            messagebox.showinfo("Éxito", f"Equipo '{equipo.nombre_equipo}' creado correctamente con {len(equipo.programadores)} programadores.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar(self):
        for widget in [self.nombre_equipo, self.universidad, self.lenguaje, self.tamano_equipo,
                       self.p1_nombre, self.p1_apellidos, self.p2_nombre, self.p2_apellidos,
                       self.p3_nombre, self.p3_apellidos, self.contrasena, self.confirmacion]:
            widget.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()