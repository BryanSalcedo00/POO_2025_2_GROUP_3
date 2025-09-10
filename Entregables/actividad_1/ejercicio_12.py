# Enunciado:
# Un  empleado  trabaja  48  horas  en  la  semana  a  razón  de  $5.000  hora.
# El  porcentaje  de retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto, la retención en la fuente y el salario neto del trabajador.

# Solución:
class Calculadora_Salario:
    def __init__(self, horas_laboradas, valor_hora, retencion):
        self.horas_laboradas = horas_laboradas
        self.valor_hora = valor_hora
        self.retencion = retencion / 100
    
    def calcular_salario_bruto(self):
        salario_bruto = self.horas_laboradas*self.valor_hora
        return salario_bruto
    
    def calcular_retencion(self):
        retencion = self.calcular_salario_bruto()*self.retencion
        return retencion
    
    def calcular_salario_neto(self):
        salario_neto = self.calcular_salario_bruto() - self.calcular_retencion()
        return salario_neto
    
def main():
    while True:
        try:
            horas_laboradas = float(input("Ingrese las horas laboradas: "))
            valor_hora = float(input("Ingrese el valor por hora: "))
            retencion = float(input("Ingrese el porcentaje retencion: "))
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

    salario = Calculadora_Salario(horas_laboradas, valor_hora, retencion)
    print(f"El salario bruto es: {salario.calcular_salario_bruto()}")
    print(f"La retención es: {salario.calcular_retencion()}")
    print(f"El salario neto es: {salario.calcular_salario_neto()}")

if __name__ == "__main__":
    main()