import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Huesped:
    def __init__(self, nombre, apellidos, documento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.documento = documento


class Reserva:
    def __init__(self, fecha_ingreso, huesped, precio_por_dia):
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = None
        self.huesped = huesped
        self.precio_por_dia = precio_por_dia

    def dias_estadia(self):
        return (self.fecha_salida - self.fecha_ingreso).days

    def total_pagar(self):
        return self.dias_estadia() * self.precio_por_dia


class Habitacion:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.disponible = True
        self.reserva = None

    def ocupar(self, reserva):
        self.disponible = False
        self.reserva = reserva

    def liberar(self):
        self.disponible = True
        self.reserva = None


class Hotel:
    def __init__(self):
        self.habitaciones = []
        # primeras 5 → 120000, restantes 5 → 160000
        for i in range(1, 11):
            precio = 120000 if i <= 5 else 160000
            self.habitaciones.append(Habitacion(i, precio))

    def consultar(self):
        return self.habitaciones

    def registrar_ingreso(self, num_hab, reserva):
        hab = self.habitaciones[num_hab - 1]
        if not hab.disponible:
            raise ValueError("La habitación está ocupada.")
        hab.ocupar(reserva)

    def registrar_salida(self, num_hab, fecha_salida):
        hab = self.habitaciones[num_hab - 1]
        if hab.disponible:
            raise ValueError("La habitación no está ocupada.")
        if fecha_salida <= hab.reserva.fecha_ingreso:
            raise ValueError("La fecha de salida debe ser mayor a la de ingreso.")
        
        hab.reserva.fecha_salida = fecha_salida
        total = hab.reserva.total_pagar()
        hab.liberar()
        return total

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel - Gestión de Habitaciones")

        self.hotel = Hotel()

        tk.Button(root, text="Consultar habitaciones", width=25, height=2,
                  command=self.ventana_consulta).pack(pady=10)

        tk.Button(root, text="Salida de huésped", width=25, height=2,
                  command=self.ventana_salida).pack(pady=10)

    # ---------------------------------------------------
    # CONSULTAR HABITACIONES - INGRESO DE HUÉSPED
    # ---------------------------------------------------
    def ventana_consulta(self):
        win = tk.Toplevel()
        win.title("Habitaciones del hotel")

        cols = ("Número", "Precio", "Estado")
        tree = ttk.Treeview(win, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)

        tree.pack(padx=10, pady=10)

        for hab in self.hotel.consultar():
            estado = "Disponible" if hab.disponible else "No disponible"
            tree.insert("", tk.END, values=(hab.numero, hab.precio, estado))

        tk.Label(win, text="Número de habitación a ocupar:").pack(pady=5)
        entrada = tk.Entry(win)
        entrada.pack()

        def continuar():
            try:
                num = int(entrada.get())
                if num < 1 or num > 10:
                    raise ValueError
                hab = self.hotel.habitaciones[num - 1]
                if not hab.disponible:
                    raise ValueError("La habitación ya está ocupada.")
                self.ventana_ingreso(num)
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Continuar", command=continuar).pack(pady=10)

    # ---------------------------------------------------
    # INGRESO DE HUÉSPED
    # ---------------------------------------------------
    def ventana_ingreso(self, num_hab):
        win = tk.Toplevel()
        win.title(f"Ingreso a habitación {num_hab}")

        tk.Label(win, text="Fecha de ingreso (YYYY-MM-DD):").grid(row=0, column=0)
        fecha_e = tk.Entry(win)
        fecha_e.grid(row=0, column=1)

        tk.Label(win, text="Nombre:").grid(row=1, column=0)
        nombre = tk.Entry(win)
        nombre.grid(row=1, column=1)

        tk.Label(win, text="Apellidos:").grid(row=2, column=0)
        apellidos = tk.Entry(win)
        apellidos.grid(row=2, column=1)

        tk.Label(win, text="Documento:").grid(row=3, column=0)
        doc = tk.Entry(win)
        doc.grid(row=3, column=1)

        def guardar():
            try:
                if not nombre.get() or not apellidos.get() or not doc.get():
                    raise ValueError("Todos los campos son obligatorios.")

                fecha_ingreso = datetime.strptime(fecha_e.get(), "%Y-%m-%d").date()
                huesped = Huesped(nombre.get(), apellidos.get(), doc.get())
                precio = self.hotel.habitaciones[num_hab - 1].precio
                reserva = Reserva(fecha_ingreso, huesped, precio)

                self.hotel.registrar_ingreso(num_hab, reserva)
                messagebox.showinfo("OK", "Ingreso registrado correctamente.")
                win.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Registrar ingreso", command=guardar).grid(row=5, columnspan=2, pady=10)

    # ---------------------------------------------------
    # SALIDA DE HUÉSPED
    # ---------------------------------------------------
    def ventana_salida(self):
        win = tk.Toplevel()
        win.title("Salida del huésped")

        tk.Label(win, text="Número de habitación a entregar:").pack(pady=5)
        entrada = tk.Entry(win)
        entrada.pack()

        def continuar():
            try:
                num = int(entrada.get())
                if num < 1 or num > 10:
                    raise ValueError("Número de habitación inválido.")
                hab = self.hotel.habitaciones[num - 1]
                if hab.disponible:
                    raise ValueError("La habitación no está ocupada.")
                self.ventana_registrar_salida(num)
                win.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Continuar", command=continuar).pack(pady=10)

    # ---------------------------------------------------
    # REGISTRO DE SALIDA (CON CÁLCULO)
    # ---------------------------------------------------
    def ventana_registrar_salida(self, num_hab):
        win = tk.Toplevel()
        win.title(f"Salida de habitación {num_hab}")

        tk.Label(win, text=f"Habitación {num_hab}").grid(row=0, column=0, columnspan=2)

        tk.Label(win, text="Fecha de salida (YYYY-MM-DD):").grid(row=1, column=0)
        fecha_s = tk.Entry(win)
        fecha_s.grid(row=1, column=1)

        resultado = tk.Label(win, text="", font=("Arial", 11, "bold"))
        resultado.grid(row=3, columnspan=2, pady=10)

        def calcular():
            try:
                fecha_salida = datetime.strptime(fecha_s.get(), "%Y-%m-%d").date()
                total = self.hotel.registrar_salida(num_hab, fecha_salida)
                resultado.config(text=f"Total a pagar: ${total:,.0f}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Calcular y registrar salida", command=calcular)\
            .grid(row=2, columnspan=2, pady=10)


# ---------------------------------------------------
# INICIAR APLICACIÓN
# ---------------------------------------------------

root = tk.Tk()
app = App(root)
root.mainloop()