# Enunciado:
# Se  requiere  un  programa  que  modele  el  concepto  de  un  automóvil.  Un  automóvil tiene los siguientes atributos:
# - Marca: el nombre del fabricante.
# - Modelo: año de fabricación.
# - Motor: volumen en litros del cilindraje del motor de un automóvil.
# - Tipo de combustible: valor enumerado con los posibles valores de gasolina, bioetanol, diésel, biodiésel, gas natural.
# - Tipo  de  automóvil:  valor  enumerado  con  los  posibles  valores  de  carro de ciudad, subcompacto, compacto, familiar, ejecutivo, SUV.
# - Número de puertas: cantidad de puertas.
# - Cantidad de asientos: número de asientos disponibles que tiene el vehículo.
# - Velocidad  máxima:  velocidad  máxima  sostenida  por  el  vehículo  en km/h.
# - Color: valor enumerado con los posibles valores de blanco, negro, rojo, naranja, amarillo, verde, azul, violeta. 
# - Velocidad actual: velocidad del vehículo en un momento dado.
#
# La clase debe incluir los siguientes métodos:
# - Un  constructor  para  la  clase  Automóvil  donde  se  le  pasen  como  parámetros los valores de sus atributos.
# - Métodos get y set para la clase Automóvil.
# - Métodos  para  acelerar  una  cierta  velocidad,  desacelerar  y  frenar  (colocar la velocidad actual en cero). Es importante tener en cuenta  que  no  se  debe  acelerar  más  allá  de  la  velocidad  máxima  permitida  para  el  automóvil. 
#   De  igual  manera,  tampoco  es  posible  desacelerar a una velocidad negativa. Si se cumplen estos casos, se debe mostrar por pantalla los mensajes correspondientes.
# - Un método para calcular el tiempo estimado de llegada, utilizando como  parámetro  la  distancia  a  recorrer  en  kilómetros.  El  tiempo  estimado se calcula como el cociente entre la distancia a recorrer y la velocidad actual.
# - Un método para mostrar los valores de los atributos de un Auto-móvil en pantalla.
# - Un método main donde se deben crear un automóvil, colocar su velocidad actual en 100 km/h, aumentar su velocidad en 20 km/h, luego decrementar su velocidad en 50 km/h, y después frenar.
#   Con cada cambio de velocidad, se debe mostrar en pantalla la velocidad actual
#
# Adicional:
# - Agregar a la clase Automóvil, un atributo para determinar si el vehículo es automático o no. Agregar los métodos get y set para dicho atributo. 
# - Modificar el constructor para inicializar dicho atributo. 
# - Modificar el método acelerar para que si la velocidad máxima se sobrepase se genere una multa. Dicha multa se puede incrementar cada vez que el vehículo intenta superar la velocidad máxima permitida.
# - Agregar un método para determinar si un vehículo tiene multas y otro método para determinar el valor total de multas de un vehículo.

# Solución:

from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIONETANOL = "Bioetanol"
    DIESEL = "Diesel"
    BIODIESEL = "Biodiesel"
    GAS_NATURAL = "Gas natural"

class TipoAutomovil(Enum):
    CIUDAD = "Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = 'Ejecutivo'
    SUV = 'SUV'

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:

    def __init__(self, marca:str, modelo:int, motor:int, tipo_combustible:TipoCombustible, tipo_automovil:TipoAutomovil, numero_puertas:int, cantidad_asientos:int, velocidad_maxima:int, color:Color, velocidad_actual:int, es_automatico:bool, cantidad_multas:int):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual
        self.es_automatico = es_automatico
        self.cantidad_multas = cantidad_multas

    def acelerar(self, cantidad):
        if(self.velocidad_actual + cantidad <= self.velocidad_maxima):
            self.velocidad_actual += cantidad
            print(f"La velocidad aumentó {cantidad} km/h. Velocidad actual: {self.velocidad_actual} km/h")
        else:
            self.cantidad_multas += 1
            print("MULTA GENERADA: No se puede acelerar más allá del límite de velocidad")

    def desacelerar(self, cantidad):
        if(self.velocidad_actual - cantidad >= 0):
            self.velocidad_actual -= cantidad
            print(f"La velocidad disminuyó {cantidad} km/h. Velocidad actual: {self.velocidad_actual} km/h")
        else:
            print("No se puede disminuir a una velocidad a una negativa")

    def frenar(self):
        self.velocidad_actual = 0
        print(f"El automóvil se ha detenido. Velocidad actual: {self.velocidad_actual} km/h")

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            print("El automóvil está detenido. No se puede calcular el tiempo de llegada")
        else:
            tiempo_horas = distancia / self.velocidad_actual
            horas = int(tiempo_horas)
            minutos = int((tiempo_horas - horas) * 60)
            print(f"El tiempo de llegada estimado es: {horas} hora(s) y {minutos} minuto(s)")

    def mostrar_atributos(self):
        print(f'''Marca: {self.marca}\nModelo: {self.modelo}\nMotor: {self.motor}\nTipo de combustible: {self.tipo_combustible.value}\ntipo_automovil: {self.tipo_automovil.value}\nNúmero de puertas: {self.numero_puertas}\nCantidad de asientos: {self.cantidad_asientos}\nVelocidad máxima: {self.velocidad_maxima}\nColor: {self.color.value}\nEs automático: {self.es_automatico}\nCantidad de multas: {self.cantidad_multas}\nVelocidad actual: {self.velocidad_actual} km/h''')

    def tiene_multas(self):
        if self.cantidad_multas > 0:
            return True
        else:
            False
    
    def mostrar_cantidad_multas(self):
        print(f"Cantidad de multas: {self.cantidad_multas}")

def main():
    auto_1 = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL, TipoAutomovil.EJECUTIVO, 5, 6, 250, Color.NEGRO, 100, True, 0)
    auto_1.mostrar_atributos()
    auto_1.acelerar(20)
    auto_1.desacelerar(50)
    auto_1.frenar()

if __name__ == "__main__":
    main()