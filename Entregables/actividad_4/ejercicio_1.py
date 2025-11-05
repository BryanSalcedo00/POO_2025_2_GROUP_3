import tkinter as tk
from tkinter import scrolledtext

class PruebaExcepciones:
    """Simula manejo de excepciones aritméticas"""
    
    def ejecutar(self, numerador, denominador):
        if denominador == 0:
            raise ZeroDivisionError("División por cero")
        return numerador / denominador


class ExcepcionFueraLimite:
    """Simula una excepción al acceder fuera del índice de una cadena"""
    
    def ejecutar(self, texto):
        if not texto:
            raise ValueError("El texto no puede estar vacío")
        if len(texto) > 14:
            raise IndexError("Texto demasiado largo, máximo 14 caracteres")
        return texto


class ExcepcionFormatoNumero:
    """Simula la conversión de un texto a número entero"""
    
    def ejecutar(self, texto):
        try:
            numero = int(texto)
            return numero
        except ValueError:
            raise ValueError("Excepción de formato de número")
        finally:
            # Siempre se ejecuta
            print("Ingresando al finally de ExcepcionFormatoNumero")


class ProgramaPrincipal:
    """Clase principal que integra las demás clases"""

    def __init__(self):
        self.prueba = PruebaExcepciones()
        self.fuera_limite = ExcepcionFueraLimite()
        self.formato_numero = ExcepcionFormatoNumero()

    def ejecutar_todo(self, numerador, denominador, texto, texto_numero):
        salida = []

        # División
        try:
            numerador = float(numerador)
            denominador = float(denominador)
            resultado = self.prueba.ejecutar(numerador, denominador)
            salida.append(f"Resultado de la división: {resultado}")
        except ValueError:
            salida.append("Ingrese números válidos para numerador y denominador")
        except ZeroDivisionError as e:
            salida.append(f"Error: {e}")

        # Texto
        try:
            resultado_texto = self.fuera_limite.ejecutar(texto)
            salida.append(f"Texto ingresado válido: {resultado_texto}")
        except ValueError as e:
            salida.append(f"Error: {e}")
        except IndexError as e:
            salida.append(f"Error: {e}")

        # Conversión a número
        try:
            numero_convertido = self.formato_numero.ejecutar(texto_numero)
            salida.append(f"Texto convertido a número: {numero_convertido}")
        except ValueError as e:
            salida.append(f"Error: {e}")

        return "\n".join(salida)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo de Excepciones")
        self.geometry("600x400")

        self.programa = ProgramaPrincipal()

        # Campos de entrada
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="Numerador:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_numerador = tk.Entry(frame, width=10)
        self.entry_numerador.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Denominador:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_denominador = tk.Entry(frame, width=10)
        self.entry_denominador.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame, text="Texto:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_texto = tk.Entry(frame, width=30)
        self.entry_texto.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        tk.Label(frame, text="Texto a convertir a número:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_texto_numero = tk.Entry(frame, width=30)
        self.entry_texto_numero.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        # Botones
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.pack(pady=5)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        btn_limpiar.pack(pady=5)

        # Área de salida
        self.texto_salida = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=70, height=12)
        self.texto_salida.pack(padx=10, pady=10)

    def limpiar(self):
        self.texto_salida.delete("1.0", tk.END)
        self.entry_numerador.delete(0, tk.END)
        self.entry_denominador.delete(0, tk.END)
        self.entry_texto.delete(0, tk.END)
        self.entry_texto_numero.delete(0, tk.END)

    def calcular(self):
        numerador = self.entry_numerador.get()
        denominador = self.entry_denominador.get()
        texto = self.entry_texto.get()
        texto_numero = self.entry_texto_numero.get()

        resultado = self.programa.ejecutar_todo(numerador, denominador, texto, texto_numero)
        self.texto_salida.delete("1.0", tk.END)
        self.texto_salida.insert(tk.END, resultado)


if __name__ == "__main__":
    app = App()
    app.mainloop()