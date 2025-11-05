import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog

class LeerArchivo:
    """Clase que permite leer archivos de texto y mostrar su contenido."""

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer(self):
        """Lee el contenido del archivo y lo retorna como string."""
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                return contenido
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo '{self.ruta_archivo}' no existe.")
        except Exception as e:
            raise e

    def leer_mayusculas(self):
        """Lee el contenido del archivo y lo retorna todo en mayúsculas."""
        contenido = self.leer()
        return contenido.upper()

class AplicacionLeerArchivo:
    """Interfaz gráfica para mostrar y convertir archivos de texto."""

    def __init__(self, root):
        self.root = root
        self.root.title("Lector de Archivos")

        # Entrada del archivo
        self.label_archivo = tk.Label(root, text="Archivo:")
        self.label_archivo.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.entry_archivo = tk.Entry(root, width=50)
        self.entry_archivo.grid(row=0, column=1, padx=5, pady=5)

        self.boton_examinar = tk.Button(root, text="Examinar", command=self.seleccionar_archivo)
        self.boton_examinar.grid(row=0, column=2, padx=5, pady=5)

        # Área de texto
        self.text_area = scrolledtext.ScrolledText(root, width=70, height=20)
        self.text_area.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Botones
        self.boton_leer = tk.Button(root, text="Leer Archivo", command=self.mostrar_contenido)
        self.boton_leer.grid(row=2, column=0, padx=5, pady=5)

        self.boton_mayusculas = tk.Button(root, text="Mostrar Mayúsculas", command=self.mostrar_mayusculas)
        self.boton_mayusculas.grid(row=2, column=1, padx=5, pady=5)

        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.grid(row=2, column=2, padx=5, pady=5)

    def seleccionar_archivo(self):
        archivo = filedialog.askopenfilename(title="Seleccione un archivo de texto", filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            self.entry_archivo.delete(0, tk.END)
            self.entry_archivo.insert(0, archivo)

    def mostrar_contenido(self):
        ruta = self.entry_archivo.get()
        if not ruta:
            messagebox.showwarning("Advertencia", "Debe ingresar un archivo")
            return
        lector = LeerArchivo(ruta)
        try:
            contenido = lector.leer()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_mayusculas(self):
        ruta = self.entry_archivo.get()
        if not ruta:
            messagebox.showwarning("Advertencia", "Debe ingresar un archivo")
            return
        lector = LeerArchivo(ruta)
        try:
            contenido = lector.leer_mayusculas()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar(self):
        self.entry_archivo.delete(0, tk.END)
        self.text_area.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionLeerArchivo(root)
    root.mainloop()
