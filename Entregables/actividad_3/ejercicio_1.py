import tkinter as tk
from tkinter import messagebox
from statistics import mean, stdev

class CalculadoraDeNotas:
    def calcular_promedio(self, notas):
        return mean(notas)

    def calcular_desviacion(self, notas):
        return stdev(notas)

    def obtener_mayor(self, notas):
        return max(notas)

    def obtener_menor(self, notas):
        return min(notas)

class NotaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Notas del Estudiante")

        self.calc = CalculadoraDeNotas()

        self.labels = []
        self.entries = []

        for i in range(5):
            label = tk.Label(root, text=f"Nota {i + 1}:")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.labels.append(label)
            self.entries.append(entry)

        self.btn_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=5, column=0, columnspan=2, pady=10)

        self.resultado = tk.Label(root, text="", fg="black", justify="left")
        self.resultado.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def calcular(self):
        notas = []
        for i, entry in enumerate(self.entries):
            valor = entry.get().strip()
            if valor == "":
                messagebox.showerror("Error", f"La nota {i + 1} está vacía. Por favor ingrésala.")
                return
            try:
                nota = float(valor)
                notas.append(nota)
            except ValueError:
                messagebox.showerror("Error", f"La nota {i + 1} no es un número válido.")
                return

        promedio = self.calc.calcular_promedio(notas)
        desviacion = self.calc.calcular_desviacion(notas)
        nota_max = self.calc.obtener_mayor(notas)
        nota_min = self.calc.obtener_menor(notas)

        resultado_texto = (
            f"Promedio: {promedio:.2f}\n"
            f"Desviación Estándar: {desviacion:.2f}\n"
            f"Mayor Nota: {nota_max:.2f}\n"
            f"Menor Nota: {nota_min:.2f}"
        )

        self.resultado.config(text=resultado_texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotaApp(root)
    root.mainloop()