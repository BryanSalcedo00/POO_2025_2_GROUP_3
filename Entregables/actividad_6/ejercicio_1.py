import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Empleado:
    def __init__(self, nombre, apellidos, cargo, genero,
                 salario_dia, dias_trabajados, otros_ingresos,
                 salud, pension):
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.genero = genero
        self.salario_dia = salario_dia
        self.dias_trabajados = dias_trabajados
        self.otros_ingresos = otros_ingresos
        self.salud = salud
        self.pension = pension

    def salario_mensual(self):
        return (self.dias_trabajados * self.salario_dia) + \
               self.otros_ingresos - self.salud - self.pension


class Nomina:
    def __init__(self):
        self.empleados = []

    def agregar(self, empleado):
        self.empleados.append(empleado)

    def total_nomina(self):
        return sum(e.salario_mensual() for e in self.empleados)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Nómina")

        self.nomina = Nomina()

        # Botones principales
        tk.Button(root, text="Agregar empleado", width=25, height=2,
                  command=self.agregar_empleado_window).pack(pady=10)

        tk.Button(root, text="Calcular nómina", width=25, height=2,
                  command=self.calcular_nomina_window).pack(pady=10)

        tk.Button(root, text="Guardar archivo", width=25, height=2,
                  command=self.guardar_archivo).pack(pady=10)

    def agregar_empleado_window(self):
        win = tk.Toplevel()
        win.title("Agregar empleado")

        labels = [
            "Nombre:", "Apellidos:", "Cargo:",
            "Género:", "Salario por día:",
            "Días trabajados:", "Otros ingresos:",
            "Pagos por salud:", "Aporte pensiones:"
        ]

        for i, text in enumerate(labels):
            tk.Label(win, text=text).grid(row=i, column=0, padx=10, pady=5)

        nombre = tk.Entry(win)
        apellidos = tk.Entry(win)

        cargo = tk.StringVar()
        cargo_box = ttk.Combobox(win, textvariable=cargo,
                                 values=["Directivo", "Estratégico", "Operativo"])

        genero = tk.StringVar()
        genero_box = ttk.Combobox(win, textvariable=genero,
                                  values=["Masculino", "Femenino"])

        salario_dia = tk.Entry(win)
        dias_trabajados = tk.Spinbox(win, from_=1, to=31)
        otros_ingresos = tk.Entry(win)
        salud = tk.Entry(win)
        pension = tk.Entry(win)

        widgets = [
            nombre, apellidos, cargo_box, genero_box, salario_dia,
            dias_trabajados, otros_ingresos, salud, pension
        ]

        for i, w in enumerate(widgets):
            w.grid(row=i, column=1, padx=10, pady=5)

        def guardar():
            try:
                emp = Empleado(
                    nombre.get(),
                    apellidos.get(),
                    cargo.get(),
                    genero.get(),
                    float(salario_dia.get()),
                    int(dias_trabajados.get()),
                    float(otros_ingresos.get()),
                    float(salud.get()),
                    float(pension.get())
                )
                self.nomina.agregar(emp)
                messagebox.showinfo("OK", "Empleado agregado exitosamente")
                win.destroy()
            except Exception:
                messagebox.showerror("Error", "Datos inválidos, revisa los campos numéricos")

        tk.Button(win, text="Guardar", command=guardar).grid(row=10, columnspan=2, pady=10)

    def calcular_nomina_window(self):
        win = tk.Toplevel()
        win.title("Nómina de empleados")

        cols = ("Nombre", "Apellidos", "Sueldo")
        table = ttk.Treeview(win, columns=cols, show="headings")
        for col in cols:
            table.heading(col, text=col)

        table.pack(padx=10, pady=10)

        # Añadir filas
        for emp in self.nomina.empleados:
            table.insert("", tk.END, values=(emp.nombre, emp.apellidos, round(emp.salario_mensual(), 2)))

        total = self.nomina.total_nomina()

        tk.Label(win, text=f"Total de la nómina: {round(total, 2)}",
                 font=("Arial", 12, "bold")).pack(pady=10)

    def guardar_archivo(self):
        carpeta = filedialog.askdirectory()
        if not carpeta:
            return

        ruta = carpeta + "/Nomina.txt"

        with open(ruta, "w", encoding="utf-8") as f:
            f.write("----- NÓMINA DE EMPLEADOS -----\n\n")
            for e in self.nomina.empleados:
                f.write(f"{e.nombre} {e.apellidos} - Sueldo: {round(e.salario_mensual(), 2)}\n")

            f.write("\nTOTAL NÓMINA: " + str(round(self.nomina.total_nomina(), 2)))

        messagebox.showinfo("Guardado", "Archivo Nomina.txt creado correctamente")

root = tk.Tk()
app = App(root)
root.mainloop()