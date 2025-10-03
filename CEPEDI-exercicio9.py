#dado uma lista vazia peça ao usuario que digite varios valores (ate digitar "fim")
# salve os a medida que forem informados em uma lista.
# Depois peça uma posiçao e remova o elemento desta posiçao e imprima uma lista final.

lista = []
while True:
    entrada = (str(input("Digite um valor: ")))
    lista.append(entrada)
    if entrada == "fim":
        informe = int(input("Digite uma posiçao: "))
        lista.pop()
        lista.pop(informe)
        print(lista)
        break