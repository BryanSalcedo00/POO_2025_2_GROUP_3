# Enunciado:
# Se requiere un programa que modele el concepto de una persona. Una per-sona posee nombre, apellido, número de documento de identidad y año de nacimiento. La clase debe tener un constructor que inicialice los valores de sus respectivos atributos.
# La clase debe incluir los siguientes métodos:
# - Definir un método que imprima en pantalla los valores de los atri-butos del objeto.
# - En un método main se deben crear dos personas y mostrar los va-lores de sus atributos en pantalla.
#
# Adicional:
# - Agregar dos nuevos atributos a la clase Persona. Un atributo que represente  el  país  de  nacimiento  de  la  persona  (de  tipo  String)  y  otro que identifique el género de la persona, el cual debe representarse como un char con valores 'H' o 'M'.
# - Modificar el constructor de la clase Persona para que inicialice estos dos nuevos atributos
# - Modificar el método imprimir de la clase Persona para que mues-tre en pantalla los valores de los nuevos atributos.

# Solución:

class Persona:

    def __init__(self, nombre:str, apellido:str, id:int, yob:int, genero:str, pais:str):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.yob = yob
        self.genero = genero
        self.pais = pais

    def mostrar_datos_personales(self):
        print(f'''Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero de identificación: {self.id}\nAño de nacimiento: {self.yob}\nGénero: {self.genero}\nPaís: {self.pais}\n''')

def main():
        persona_1 = Persona("Bryan", "Salcedo", 1003504315, 2000, "H", "Colombia")
        persona_2 = Persona("Edinson", "Salcedo", 92507482, 1966, "H", "Colombia")
        persona_1.mostrar_datos_personales()
        persona_2.mostrar_datos_personales()

if __name__ == "__main__":
    main()