#crie uma funçao para calcular um imposto sobre determinado valor,
# caso o valor seja menor que 1000 o imposto é de 10% p
# para valores ate 2000 o imposto é de 13%
# acima de 2000 o imposto é de 15%

def calculoImposto(valor):
    if valor < 1000:
        imposto = valor * 0.1

    elif valor < 2000:
        imposto = valor * 0.13

    else:
        imposto = valor * 0.15

    return imposto

valor= int(input("Digite o valor a calcular: "))
valorFinal = calculoImposto(valor)
print(valorFinal)

