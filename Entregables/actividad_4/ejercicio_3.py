import tkinter as tk
from tkinter import messagebox
import math

class CalculosNumericos:
    """Clase con métodos estáticos para cálculos matemáticos con excepciones."""
    
    @staticmethod
    def logaritmo(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser positivo para calcular logaritmo")
        return math.log(valor)
    
    @staticmethod
    def raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser no negativo para calcular raíz cuadrada")
        return math.sqrt(valor)
    
    @staticmethod
    def pendiente(x1, y1, x2, y2):
        if x2 - x1 == 0:
            raise ArithmeticError("División por cero al calcular la pendiente")
        return (y2 - y1) / (x2 - x1)
    
    @staticmethod
    def punto_medio(x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    @staticmethod
    def raices_cuadratica(a, b, c):
        if a == 0:
            raise ArithmeticError("El coeficiente a no puede ser cero")
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            raise ArithmeticError("Raíces complejas no permitidas")
        raiz_disc = math.sqrt(discriminante)
        x1 = (-b + raiz_disc) / (2*a)
        x2 = (-b - raiz_disc) / (2*a)
        return x1, x2
    
    @staticmethod
    def convertir_base(numero, base_destino):
        if base_destino < 2 or base_destino > 36:
            raise ValueError("La base debe estar entre 2 y 36")
        if numero == 0:
            return "0"
        cifras = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        num = numero
        while num > 0:
            resultado = cifras[num % base_destino] + resultado
            num //= base_destino
        return resultado

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Cálculos Numéricos")

        # Entradas
        tk.Label(master, text="Número para logaritmo/raíz:").grid(row=0, column=0)
        self.valor_entry = tk.Entry(master)
        self.valor_entry.grid(row=0, column=1)

        tk.Label(master, text="Punto x1, y1:").grid(row=1, column=0)
        self.x1_entry = tk.Entry(master, width=5)
        self.x1_entry.grid(row=1, column=1, sticky='W')
        self.y1_entry = tk.Entry(master, width=5)
        self.y1_entry.grid(row=1, column=1, sticky='E')

        tk.Label(master, text="Punto x2, y2:").grid(row=2, column=0)
        self.x2_entry = tk.Entry(master, width=5)
        self.x2_entry.grid(row=2, column=1, sticky='W')
        self.y2_entry = tk.Entry(master, width=5)
        self.y2_entry.grid(row=2, column=1, sticky='E')

        tk.Label(master, text="Ecuación cuadrática a,b,c:").grid(row=3, column=0)
        self.a_entry = tk.Entry(master, width=5)
        self.a_entry.grid(row=3, column=1, sticky='W')
        self.b_entry = tk.Entry(master, width=5)
        self.b_entry.grid(row=3, column=1)
        self.c_entry = tk.Entry(master, width=5)
        self.c_entry.grid(row=3, column=1, sticky='E')

        tk.Label(master, text="Número a convertir:").grid(row=4, column=0)
        self.numero_entry = tk.Entry(master)
        self.numero_entry.grid(row=4, column=1)

        tk.Label(master, text="Base de destino:").grid(row=5, column=0)
        self.base_entry = tk.Entry(master)
        self.base_entry.grid(row=5, column=1)

        # Botones
        tk.Button(master, text="Calcular", command=self.calcular).grid(row=6, column=0)
        tk.Button(master, text="Limpiar", command=self.limpiar).grid(row=6, column=1)

        # Resultados
        self.resultados_text = tk.Text(master, height=15, width=60)
        self.resultados_text.grid(row=7, column=0, columnspan=2)

    def calcular(self):
        self.resultados_text.delete('1.0', tk.END)
        try:
            valor = float(self.valor_entry.get())
            log_val = CalculosNumericos.logaritmo(valor)
            raiz_val = CalculosNumericos.raiz_cuadrada(valor)
            self.resultados_text.insert(tk.END, f"Logaritmo: {log_val}\n")
            self.resultados_text.insert(tk.END, f"Raíz cuadrada: {raiz_val}\n")
        except Exception as e:
            self.resultados_text.insert(tk.END, f"Error log/raíz: {e}\n")

        try:
            x1, y1 = float(self.x1_entry.get()), float(self.y1_entry.get())
            x2, y2 = float(self.x2_entry.get()), float(self.y2_entry.get())
            pendiente = CalculosNumericos.pendiente(x1, y1, x2, y2)
            punto_medio = CalculosNumericos.punto_medio(x1, y1, x2, y2)
            self.resultados_text.insert(tk.END, f"Pendiente: {pendiente}\n")
            self.resultados_text.insert(tk.END, f"Punto medio: {punto_medio}\n")
        except Exception as e:
            self.resultados_text.insert(tk.END, f"Error pendiente/punto medio: {e}\n")

        try:
            a, b, c = float(self.a_entry.get()), float(self.b_entry.get()), float(self.c_entry.get())
            raices = CalculosNumericos.raices_cuadratica(a, b, c)
            self.resultados_text.insert(tk.END, f"Raíces cuadráticas: {raices}\n")
        except Exception as e:
            self.resultados_text.insert(tk.END, f"Error raíces cuadráticas: {e}\n")

        try:
            numero = int(self.numero_entry.get())
            base = int(self.base_entry.get())
            conversion = CalculosNumericos.convertir_base(numero, base)
            self.resultados_text.insert(tk.END, f"Número {numero} en base {base}: {conversion}\n")
        except Exception as e:
            self.resultados_text.insert(tk.END, f"Error conversión base: {e}\n")

    def limpiar(self):
        self.valor_entry.delete(0, tk.END)
        self.x1_entry.delete(0, tk.END)
        self.y1_entry.delete(0, tk.END)
        self.x2_entry.delete(0, tk.END)
        self.y2_entry.delete(0, tk.END)
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.c_entry.delete(0, tk.END)
        self.numero_entry.delete(0, tk.END)
        self.base_entry.delete(0, tk.END)
        self.resultados_text.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()