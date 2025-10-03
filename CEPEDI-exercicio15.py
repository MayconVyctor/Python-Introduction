#Crie uma funçao em python que verifique se um ano informado é bisesxto

def verificarAnoBissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        print("Ano bissexto")

    elif ano % 400 == 0:
        print("Ano bissexto")

    else:
        print("Ano nao é bissexto")

ano = int(input("Digite o ano para verificar: "))
print(verificarAnoBissexto(ano))
