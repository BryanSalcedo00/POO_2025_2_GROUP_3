# Enunciado: 
# A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele a Juan su edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la edad de Juan y mi edad es la suma de las tres. 
# Hacer un algoritmo que muestre la edad de los cuatro.

# Solución:
class Persona:
    def __init__(self, nombre, edad=0):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"{self.nombre} tiene {round(self.edad)} años")

def main():
    try:
        edad_juan = float(input("Ingrese la edad de Juan: "))

        juan = Persona("Juan", edad_juan)
        alberto = Persona("Alberto", (2/3) * edad_juan)
        ana = Persona("Ana", (4/3) * edad_juan)
        mama = Persona("Mamá", juan.edad + alberto.edad + ana.edad)

        juan.mostrar_datos()
        alberto.mostrar_datos()
        ana.mostrar_datos()
        mama.mostrar_datos()

    except ValueError:
        print("Error: Por favor, ingrese un número válido para la edad")

if __name__ == "__main__":
    main()