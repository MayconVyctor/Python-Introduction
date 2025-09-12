#crie um algoritmo que solicite ao usuario 2 valores, e em seguida troque o valor dessas variaveis e imprima os novos valores

num1 = int(input("Insira sua nota 1: "))
num2 = int(input("Insira sua nota 2: "))

temporario = num1
num1=num2
num2=temporario

print(num1)
print(num2)