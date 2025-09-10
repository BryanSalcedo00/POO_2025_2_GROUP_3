# Enunciado: 
# Hacer un seguimiento (prueba de escritorio) del siguiente grupo de instrucciones:
#   INICIO 
#     SUMA = 0   
#     X = 20  
#     SUMA = SUMA + X   
#     Y = 40  
#     X = X + Y ** 2  
#     SUMA = SUMA + X / Y   
#     ESCRIBA: “EL VALOR DE LA SUMA ES:”, SUMA 
#   FIN_INICIO

# Solución:
class Calculadora:
    def __init__(self, suma, x, y):
        self.suma = suma
        self.x = x
        self.y = y

    def calcular(self):
        try:
            self.suma += self.x
            self.x = self.x + self.y ** 2
            self.suma += self.x / self.y
        except ZeroDivisionError:
            print("Error: División por cero no permitida.")
            self.suma = None

    def mostrar_resultado(self):
        if self.suma is not None:
            print(f"El valor de la suma es: {self.suma}")
        else:
            print("No se pudo calcular la suma debido a un error.")


def main():
    while True:
        try:
            suma = float(input("Ingrese el valor inicial de SUMA: "))
            x = float(input("Ingrese el valor de X: "))
            y = float(input("Ingrese el valor de Y: "))
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido")

    calc = Calculadora(suma, x, y)
    calc.calcular()
    calc.mostrar_resultado()


if __name__ == "__main__":
    main()