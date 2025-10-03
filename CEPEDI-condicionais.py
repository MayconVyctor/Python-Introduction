#faça um algoritmo que leia um numero dito pole usuario e se for maior que 20 imprima a metade dele


"""
num1 = float(input("Digite um numero: "))

if num1 > 20:
    print(num1/2)

print("numero original" ,num1)
"""
"""

num1= int(input("Digite um numero: "))

if num1 % 2 == 0:
    print("O numero ", num1, "é par")

"""
# O usuario vai informar um horario inicial e um horario final, dentro do mesmo dia. O horario inicial sempre sera menor ou igual o horario final
# para isso leia 4 numeros referentes a hora e minuto inicial, e hora e minuto final.Calcule e escreva na tela o numero de minutos entre os 2 horarios informddos
"""
horario1 = int(input("Digite um horario inicial: "))
minuto1 = int(input("Digite um minuto inicial: "))
horario2 = int(input("Digite o horario final: "))
minuto2 = int(input("Digite o minuto final: "))


if minuto2 >= minuto1:
    minutosH = (horario2 - horario1) *60
    minutosM = (minuto2 - minuto1)
    diferencaMinutos =  minutosH + minutosM
    print(" A diferencça em minutos é: " ,diferencaMinutos, " minutos")

else:
    horarioInicial = horario1 *60 + minuto1
    horarioFinal = horario2 *60 + minuto2
    diferencaMinutos = horarioFinal- horarioInicial
    print(" A diferencça em minutos é ", diferencaMinutos, " minutos")
"""

#informe 3 numeros e verifique quantos deles sao maior que zero

""""
num1 = int(input("Digite o 1 numero: "))
num2 = int(input("Digite o 2 numero: "))
num3 = int(input("Digite o 3 numero: "))

cont = 0

if num1 >= 0:
   cont = cont + 1

if num2 >= 0:
    cont = cont + 1

if num3 >= 0:
     cont = cont + 1

print(cont)
"""""

"""""
num1 = int(input("Digite o 1 numero: "))
num2 = int(input("Digite o 2 numero: "))
num3 = int(input("Digite o 3 numero: "))

cont = 0

if num1 % 2 != 0 :
   cont = cont + 1

if num1 % 2 != 0 :
    cont = cont + 1

if num1 % 2 != 0 :
     cont = cont + 1

print(cont)
"""""
"""""
num1 = int(input("Digite o 1 numero: "))
num2 = int(input("Digite o 2 numero: "))
num3 = int(input("Digite o 3 numero: "))

soma = 0

if num1 % 2 != 0 :
   soma = soma + num1

if num1 % 2 != 0 :
    soma = soma + num2

if num1 % 2 != 0 :
     soma = soma + num3

print(soma)

"""""

#criança 0-12
#adoloscente 12-17
#adulto 18-59
#idoso acima de 60

"""""
idade = int(input("Digite a idade: "))

if idade >= 0 and idade < 13 :
    print("Criança")

if idade >= 13 and idade < 18:
    print("Adolescente")

if idade >= 18 and idade < 60:
    print("Adulto")

else:
    print("Idoso")
"""""

#imc indice de massa corporea
#imc = peso / altura *altura
#imc 0 e <20 - abaixo do peso
#imc 20 e <25 - peso normal
#imc 25 a <30 - sobrepeso
#imc acima de 30 - obesidade

"""""
peso = float(input("Digite o peso: "))
altura = float(input("Digite o altura: "))

imc = peso / (altura * altura)

if imc < 20:
    print("abaixo do peso, seu imc é: ", imc)

elif imc < 25:
    print ("peso normal, seu imc é: ",imc)

elif imc < 30:
    print("sobrepeso, seu imc é: ", imc)

else:
    print("obesidade")
"""
salario = float(input("Digite o salario: "))

if salario > 3036 < 3533.31 :
    salario = salario * 0.075/100
    print(salario)

elif salario < 4688.85:
    salario = salario * 0.15/100
    print(salario)

elif salario < 5830.85 :
    salario = salario * 0.225/100
    print(salario)

else:
    salario = salario * 0.275/100
    print(salario)