# Enunciado: Elabore un algoritmo que lea un número y obtenga su cuadrado y su cubo.

# Solución:
class Calculadora:
    def __init__(self, numero):
        self.numero = numero

    def calcular_cuadrado(self):
        cuadrado = self.numero**2
        return cuadrado
    
    def calcular_cubo(self):
        cubo = self.numero**3
        return cubo

def main():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            calc = Calculadora(numero)
            print(f"El cuadrado es: {calc.calcular_cuadrado()}")
            print(f"El cubo es: {calc.calcular_cubo()}")
            break  # salir del bucle si todo va bien
        except ValueError:
            print("Error: Por favor ingrese un número válido")

if __name__ == "__main__":
    main()