# Instruçoes de repetiçoes
#   condicao -> while (enquanto)
#   quantidade de passos -> for (para) nao sabe quantas vezes vai executar
#

#Laço/loop infinito
#x = 20
#while x > 10:
#    print("tamo programando tamo programando")


#valor = float(input("Digite um valor: "))
#soma = 0#

#while valor != 0:
#   soma = valor + soma
#    valor = int(input("Digite um numero: "))

#print("A soma é: ",soma)


#for idade in range(5, 10, 1):
#    print(idade)

#fazer um for que imprima todos os numeros pares entre 1 e 50, inclusive

num1 = int(input("Digite outro numero: "))
num2 = int(input("Digite outro numero: "))

for i in range(num1, num2,):
    if i % 2 == 0:
        print("os numeros pares são: ",i)
#    elif i % 2 != 0:
#        print("os numeros impares sao: ",i)
print("Fim do loop")

#faça um programa em python que imprima os numeros de 1 a 100, pulando os mutiplos de 7
