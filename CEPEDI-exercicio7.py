#faça um programa em python que imprima os numeros de 1 a 100, pulando os mutiplos de 7

#for i in range(1,100):
#    if i % 7 != 0:
#        print(i)

#faça um programa que leia uma quantidade de numeros de entrada em seguida leia estes numeros, ao final imprima o maior e o menor numero lido

numeroDeLaços = int(input("Digite um numero de laços: "))
maior = -10000 #sys.float_info.min
menor = 10000 #sys.float_info.max

for i in range(numeroDeLaços):
    numero = int(input(f"Digite um numero: {i+1}: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f"O maior numero é {maior}. e o menor numero é {menor}")