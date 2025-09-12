#volume de uma caixa de agua
import math
altura = float(input("Insira sua altura: "))
raio = float(input("Insira sua raio: "))
pi = math.pi
raioBase = pi * raio **2

volume = raioBase * altura

volumeLitros = volume * 1000
print(volumeLitros)
