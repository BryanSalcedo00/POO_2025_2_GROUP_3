import tkinter as tk
from tkinter import messagebox, scrolledtext

class Vendedor:
    """Clase que representa un vendedor con validación de edad."""

    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.verificar_edad(edad)

    def imprimir(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}"

    def verificar_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")

class TablaASCII:
    """Clase para almacenar símbolos y sus valores numéricos."""
    
    def __init__(self):
        self.tabla = {}  # Diccionario vacío
    
    def set(self, simbolo, numero):
        if simbolo is None or numero is None:
            raise ValueError("Símbolo y número no pueden ser nulos")
        self.tabla[simbolo] = numero

    def get(self, simbolo):
        if simbolo not in self.tabla:
            raise KeyError(f"Símbolo '{simbolo}' no existe en la tabla")
        return self.tabla[simbolo]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Vendedor y Tabla ASCII")
        self.geometry("600x500")

        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Apellidos:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_apellidos = tk.Entry(self)
        self.entry_apellidos.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_edad = tk.Entry(self)
        self.entry_edad.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text="Símbolo:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_simbolo = tk.Entry(self)
        self.entry_simbolo.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text="Número:").grid(row=4, column=0, padx=5, pady=5)
        self.entry_numero = tk.Entry(self)
        self.entry_numero.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(self, text="Crear Vendedor", command=self.crear_vendedor).grid(row=5, column=0, padx=5, pady=10)
        tk.Button(self, text="Agregar a Tabla ASCII", command=self.agregar_ascii).grid(row=5, column=1, padx=5, pady=10)
        tk.Button(self, text="Consultar ASCII", command=self.consultar_ascii).grid(row=6, column=0, padx=5, pady=10)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=6, column=1, padx=5, pady=10)

        self.salida = scrolledtext.ScrolledText(self, width=70, height=15)
        self.salida.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.tabla_ascii = TablaASCII()

    def crear_vendedor(self):
        try:
            nombre = self.entry_nombre.get()
            apellidos = self.entry_apellidos.get()
            edad = int(self.entry_edad.get())
            vendedor = Vendedor(nombre, apellidos, edad)
            self.salida.insert(tk.END, f"Vendedor creado correctamente:\n{vendedor.imprimir()}\n\n")
        except ValueError as e:
            messagebox.showerror("Error de Vendedor", str(e))


    def agregar_ascii(self):
        try:
            simbolo = self.entry_simbolo.get()
            numero = int(self.entry_numero.get())
            self.tabla_ascii.set(simbolo, numero)
            self.salida.insert(tk.END, f"Símbolo '{simbolo}' agregado con valor {numero}\n\n")
        except ValueError as e:
            messagebox.showerror("Error Tabla ASCII", str(e))

    def consultar_ascii(self):
        try:
            simbolo = self.entry_simbolo.get()
            numero = self.tabla_ascii.get(simbolo)
            self.salida.insert(tk.END, f"Símbolo '{simbolo}' tiene valor {numero}\n\n")
        except KeyError as e:
            messagebox.showerror("Error Tabla ASCII", str(e))

    def limpiar(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_simbolo.delete(0, tk.END)
        self.entry_numero.delete(0, tk.END)
        self.salida.delete("1.0", tk.END)


if __name__ == "__main__":
    app = App()
    app.mainloop()