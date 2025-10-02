# Enunciado:
# Se requiere un programa que modele el concepto de un planeta del sistema solar. Un planeta tiene los siguientes atributos:
# - Un nombre de tipo Sring con valor inicial de null.
# - Cantidad de satélites de tipo int con valor inicial de cero.
# - Masa en kilogramos de tipo double con valor inicial de cero.
# - Volumen en kilómetros cúbicos de tipo double con valor inicial de cero.
# - Diámetro en kilómetros de tipo int con valor inicial de cero.
# - Distancia media al Sol en millones de kilómetros, de tipo int con valor inicial de cero.
# - Tipo de planeta de acuerdo con su tamaño, de tipo enumerado con los siguientes valores posibles: GASEOSO, TERRESTRE y ENANO.
# - Observable a simple vista, de tipo booleano con valor inicial false.
#
# La clase debe incluir los siguientes métodos:
# - La clase debe tener un constructor que inicialice los valores de sus respectivos atributos.
# - Definir un método que imprima en pantalla los valores de los atri-butos de un planeta.
# - Calcular la densidad un planeta, como el cociente entre su masa y su volumen.
# - Determinar  si  un  planeta  del  sistema  solar  se  considera  exterior.  Un planeta exterior está situado más allá del cinturón de asteroides. El cinturón de asteroides se encuentra entre 2.1 y 3.4 UA. 
#   Una unidad  astronómica  (UA)  es  la  distancia  entre  la  Tierra  y  el  Sol=  149 597 870 Km.
# - En un método main se deben crear dos planetas y mostrar los valores  de  sus  atributos  en  pantalla.  Además,  se  debe  imprimir  la  densidad de cada planeta y si el planeta es un planeta exterior del sistema solar.
#
# Adicional:
# - Agregar dos atributos a la clase Planeta. El primero debe representar  el  periodo  orbital  del  planeta  (en  años).  El  segundo  atributo  representa el periodo de rotación (en días). 
# - Modificar el constructor de la clase para que inicialice los valores de estos dos nuevos atributos.
# - Modificar  el  método  imprimir  para  que  muestre  en  pantalla  los  valores de los nuevos atributos.

# Solución:

from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:

    def __init__(self, nombre:str, cantidad_satelites:int, masa:float, volumen:float, diametro:int, distancia_al_sol:int, tipo_planeta:TipoPlaneta, es_observable:bool, periodo_orbital:int, periodo_rotacion:int):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_al_sol = distancia_al_sol
        self.tipo_planeta = tipo_planeta
        self.es_observable = es_observable
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    def mostrar_atributos(self):
        print(f'''Nombre: {self.nombre}\nCantidad de satélites: {self.cantidad_satelites}\nMasa: {self.masa:e}\nVolumen: {self.volumen:e}\nDiámetro: {self.diametro}\nDistancia al Sol: {self.distancia_al_sol}\nTipo de planeta: {self.tipo_planeta.value}\nEs observable: {self.es_observable}\nPeriodo orbital: {self.periodo_orbital}\nPeriodo de rotacion: {self.periodo_rotacion}''')

    def calcular_densidad(self):
        return self.masa/self.volumen
    
    def es_planeta_exterior(self):
        limite = 149597870 * 3.4
        if (self.distancia_al_sol > limite):
            return True
        else:
            return False

def main():
    planeta_1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000, TipoPlaneta.TERRESTRE, True, 1, 1)
    planeta_2 = Planeta("Júpiter",79, 1.899E27, 1.4313E15, 139820, 750000000,TipoPlaneta.GASEOSO, True, 12, 0)
    planeta_1.mostrar_atributos()
    print(f'Densidad: {planeta_1.calcular_densidad():e}')
    print(f'Es planeta exterior: {planeta_1.es_planeta_exterior()}\n')
    planeta_2.mostrar_atributos()
    print(f'Densidad: {planeta_2.calcular_densidad():e}')
    print(f'Es planeta exterior: {planeta_2.es_planeta_exterior()}')

if __name__ == "__main__":
    main()