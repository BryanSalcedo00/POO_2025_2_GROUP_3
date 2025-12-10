import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

# ------------------------------
# Clase Contacto
# ------------------------------
class Contacto:
    def __init__(self, nombres, apellidos, fecha_nac, direccion, telefono, correo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nac = fecha_nac
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.telefono} - {self.correo}"


# ------------------------------
# Clase Agenda
# ------------------------------
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)


# ------------------------------
# Interfaz gráfica
# ------------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contactos")

        self.agenda = Agenda()

        # Nombres
        tk.Label(root, text="Nombres:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.nombres_entry = tk.Entry(root)
        self.nombres_entry.grid(row=0, column=1, padx=5, pady=5)

        # Apellidos
        tk.Label(root, text="Apellidos:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.apellidos_entry = tk.Entry(root)
        self.apellidos_entry.grid(row=1, column=1, padx=5, pady=5)

        # Fecha de nacimiento
        tk.Label(root, text="Fecha de nacimiento:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.fecha_entry = DateEntry(root, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=2, column=1, padx=5, pady=5)

        # Dirección
        tk.Label(root, text="Dirección:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.direccion_entry = tk.Entry(root)
        self.direccion_entry.grid(row=3, column=1, padx=5, pady=5)

        # Teléfono
        tk.Label(root, text="Teléfono:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.telefono_entry = tk.Entry(root)
        self.telefono_entry.grid(row=4, column=1, padx=5, pady=5)

        # Correo
        tk.Label(root, text="Correo electrónico:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.correo_entry = tk.Entry(root)
        self.correo_entry.grid(row=5, column=1, padx=5, pady=5)

        # Botón Agregar
        tk.Button(root, text="Agregar", command=self.agregar_contacto).grid(row=6, column=0, columnspan=2, pady=10)

        # Listbox para mostrar contactos
        self.lista_contactos = tk.Listbox(root, width=70)
        self.lista_contactos.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # ------------------------------
    # Función para agregar contacto
    # ------------------------------
    def agregar_contacto(self):
        nombres = self.nombres_entry.get()
        apellidos = self.apellidos_entry.get()
        fecha_nac = self.fecha_entry.get_date()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()
        correo = self.correo_entry.get()

        # Validar campos
        if not nombres or not apellidos or not direccion or not telefono or not correo:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        contacto = Contacto(nombres, apellidos, fecha_nac, direccion, telefono, correo)
        self.agenda.agregar_contacto(contacto)

        # Actualizar lista
        self.lista_contactos.insert(tk.END, str(contacto))

        # Limpiar entradas
        self.nombres_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)


# ------------------------------
# Ejecutar aplicación
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()