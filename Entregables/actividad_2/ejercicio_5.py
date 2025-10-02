# Enunciado:
# Se  requiere  un  programa  que  modele  una  cuenta  bancaria  que  posee  los  siguientes atributos:
# - Nombres del titular.
# - Apellidos del titular.
# - Número de la cuenta bancaria.
# - Tipo  de  cuenta:  puede  ser  una  cuenta  de  ahorros  o  una  cuenta  corriente.
# - Saldo de la cuenta.
# 
# Se debe definir un constructor que inicialice los atributos de la clase. Cuando se crea una cuenta bancaria, su saldo inicial tiene un valor de cero.
# En una determinada cuenta bancaria se puede: 
# - Imprimir  por  pantalla  los  valores  de  los  atributos  de  una  cuenta  bancaria.
# - Consultar el saldo de una cuenta bancaria.
# - Consignar un determinado valor en la cuenta bancaria, actualizando el saldo correspondiente.
# - Retirar un determinado valor de la cuenta bancaria, actualizando el saldo correspondiente. Es necesario tener en cuenta que no se puede realizar el retiro si el valor solicitado supera el saldo actual de la cuenta.
#
# Adicional:
# - Agregar  a  la  clase  CuentaBancaria,  un  atributo  que  represente  el  porcentaje de interés mensual aplicado a la cuenta.
# - Agregar un método que calcule un nuevo saldo aplicando la tasa de interés correspondiente

# Solución:

from enum import Enum

class TipoCuenta(Enum):
    AHORROS = 'Ahorros'
    CORRIENTE = 'Corriente'

class CuentaBancaria:
    def __init__(self, nombre_titular: str, apellido_titular:str , numero_cuenta: int, tipo_cuenta: TipoCuenta, saldo_cuenta = 0.0, tasa_interes = 0.0):
        self.nombre_titular = nombre_titular
        self.apellido_titular = apellido_titular
        self.numero_cuenta = numero_cuenta
        self.saldo_cuenta = saldo_cuenta
        self.tasa_interes = tasa_interes
        self.tipo_cuenta = tipo_cuenta


    def mostrar_atributos(self):
        print(f'''Nombre: {self.nombre_titular}
Apellido: {self.apellido_titular}
Número de cuenta: {self.numero_cuenta}
Tipo de cuenta: {self.tipo_cuenta.value}
Saldo: {self.saldo_cuenta}
Tasa de interés mensual: {self.tasa_interes}''')

    def consultar_saldo(self):
        print(f'Saldo actual: $ {self.saldo_cuenta}')

    def consignar_saldo(self, cantidad):
        self.saldo_cuenta += cantidad
        print(f'Se consignaron $ {cantidad} en la cuenta. Nuevo saldo: $ {self.saldo_cuenta}')

    def retirar_saldo(self, cantidad):
        if (self.saldo_cuenta - cantidad <= self.saldo_cuenta):
            self.saldo_cuenta -= cantidad
            print(f'Se retiraron $ {cantidad} de la cuenta. Nuevo saldo: $ {self.saldo_cuenta} ')
        else:
            print('El valor solicitado supera el saldo de la cuenta')

    def calcular_saldo_con_interes(self):
        saldo_con_interes = self.saldo_cuenta + self.saldo_cuenta * self.tasa_interes
        print(f'El saldo total con intereses es: $ {saldo_con_interes}')

def main():
    cuenta1 = CuentaBancaria("Pedro","Pérez", 123456789, TipoCuenta.AHORROS)
    cuenta1.mostrar_atributos()
    cuenta1.consignar_saldo(200000)
    cuenta1.consignar_saldo(300000)
    cuenta1.retirar_saldo(400000)

if __name__ == '__main__':
    main()