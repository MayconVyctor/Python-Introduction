"""""
Preferencia de operadores
Prioridade de operadores

da maior prioridade para a MENOR 
OPERADORES ARITMETICOS (**, raiz. *, /, //, %, +, -)
OPERADORES RELACIONAIS (=, !=, <, <=, >, >=)
OPERADORES LÓGICOS (not, and, or)
RAIZ QUADRADA = SQAURE ROOT= SQRT 
POTENCIA = POWER = POW (BASE, EXPOENTE)

A = FALSE 
B = TRUE

not (A OR B) / NOT (A) OR B / "ERRADO"

Separialização de operações matematicas

forma da area do trapezio 
A = B*b *h /2 -sem separar
A = ((B*b) *h) /2 - com separação
"""
baseMaior= int(input("Digite a Base maior: "))
baseMenor = int(input("Digite a Base menor: "))
altura = int(input("Digite a Altura: "))

areaTrapezio = (( baseMaior+ baseMenor) * altura ) /2
print(areaTrapezio)

# converter fahrenheit para celsius
#Temp = T - T * 5 / 9

tempFahrenheit = int(input("Informe a temperatura em Fahrenheit: "))
''
temperaturaCelsius = (tempFahrenheit - 32) * 5 / 9
print("A temperatura em Celsius é ", temperaturaCelsius)

tempCelsius = int(input("Informe a temperatura em Celsius: "))
temperaturaFahrenheit = (tempCelsius * 9 / 5) + 32
print("A temperatura em Fahrenheit é ", temperaturaFahrenheit)

#funções de calculo de raiz de uma equação de segundo grau









