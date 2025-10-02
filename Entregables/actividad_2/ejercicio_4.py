# Enunciado:
# Se requiere un programa que modele varias figuras geométricas: el círculo, el rectángulo, el cuadrado y el triángulo rectángulo.
# - El círculo tiene como atributo su radio en centímetros.
# - El rectángulo, su base y altura en centímetros.
# - El cuadrado, la longitud de sus lados en centímetros.
# - El triángulo, su base y altura en centímetros.
# 
# Se requieren métodos para determinar el área y el perímetro de cada figura geométrica. Además, para el triángulo rectángulo se requiere:
#  - Un método que calcule la hipotenusa del rectángulo.
#  - Un método para determinar qué tipo de triángulo es:
#     - Equilátero: todos sus lados son iguales.
#     - Isósceles: tiene dos lados iguales.
#     - Escaleno: todos sus lados son diferentes.
# 
# Se  debe  desarrollar  una  clase  de  prueba  con  un  método  main  para  crear las cuatro figuras y probar los métodos respectivos.
#
# Adicional:
# - Agregar una nueva clase denominada Rombo. Definir los métodos para calcular el área y el perímetro de esta nueva figura geométrica.
# - Agregar una nueva clase denominada Trapecio. Definir los métodos para calcular el área y el perímetro de esta nueva figura geométrica

# Solución:

import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura

class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()
    
    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base == self.altura or self.base == hipotenusa or self.altura == hipotenusa:
            return "Isósceles"
        else:
            return "Escaleno"

class Rombo:

    def __init__(self, diagonal_mayor, diagonal_menor):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2
    
    def calcular_perimetro(self):
        return 4 * math.sqrt((self.diagonal_mayor/  2) ** 2 + (self.diagonal_menor / 2 ) ** 2)

class Trapecio:

    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
    
    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self):
        lado = math.sqrt(((self.base_mayor - self.base_menor)/2) ** 2 + self.altura ** 2)
        return self.base_mayor + self.base_menor + 2 * lado
    
class PruebaFiguras:
    def main():
        circulo = Circulo(2)
        rectangulo = Rectangulo(1, 2)
        cuadrado = Cuadrado(3)
        triangulo = Triangulo(3, 5)
        rombo = Rombo(10, 6)
        trapecio = Trapecio(12, 6, 4)
        
        print(f'''El área del círculo es: {circulo.calcular_area()}
    El perímetro del círculo es: {circulo.calcular_perimetro()}

    El área del rectángulo es: {rectangulo.calcular_area()}
    El perímetro del rectángulo es: {rectangulo.calcular_perimetro()}

    El área del cuadrado es: {cuadrado.calcular_area()}
    El perímetro del cuadrado es: {cuadrado.calcular_perimetro()}

    El área del triángulo es: {triangulo.calcular_area()}
    El perímetro del triángulo es: {triangulo.calcular_perimetro()}
    El tipo del triángulo es: {triangulo.determinar_tipo_triangulo()}

    El área del rombo es: {rombo.calcular_area()}
    El perímetro del rombo es: {rombo.calcular_perimetro()}

    El área del trapecio es: {trapecio.calcular_area()}
    El perímetro del trapecio es: {trapecio.calcular_perimetro()}
    ''')

if __name__ == '__main__':
    PruebaFiguras.main()