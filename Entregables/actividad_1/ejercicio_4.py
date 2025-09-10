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
        print("Por favor, ingrese un número válido para la edad.")

if __name__ == "__main__":
    main()