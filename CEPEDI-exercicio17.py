#Crie uma funçao que calcule o fatorial de um numero

def calculoFatorial(valor):
    for i in range (valor-1,valor,valor):
        valorFatorial = valor * i
    return valorFatorial

#informeValorFatorial = int(input("Digite o valor a calcular: "))
valorFatorial = 5
print(calculoFatorial(valorFatorial))