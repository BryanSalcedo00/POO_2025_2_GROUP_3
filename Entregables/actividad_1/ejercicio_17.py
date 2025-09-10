import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_longitud(self):
        return 2 * math.pi * self.radio


def main():
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            if radio < 0:
                print("El radio no puede ser negativo.")
                continue

            circulo = Circulo(radio)
            area = circulo.calcular_area()
            longitud = circulo.calcular_longitud()

            print(f"Área del círculo: {area:.2f}")
            print(f"Longitud de la circunferencia: {longitud:.2f}")
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()