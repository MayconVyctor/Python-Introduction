#Crie uma funcao que receba o mes (01-12) e ano e informe quantos dias tem o mes

def verificarAnoBissexto(ano):
        if ano % 4 == 0 and ano % 100 != 0 :
            print("Ano bissexto")
            anoBissexto = True
        elif  ano % 400 == 0:
            print("Ano bissexto")
            anoBissexto = True
        else:
            print("Ano nao é bissexto")
            anoBissexto = False
        return anoBissexto

def informarDiasDoMes(mes,anoBissexto):

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("O mês tem 31 dias")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print("O mês tem 30 dias")
    elif mes == 2 and anoBissexto == True:
        print("O mes tem 29 dias")
    else:
        print("O mẽs tem 28 dias")


mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))
anoBissexto = verificarAnoBissexto(ano)
informarDiasDoMes(mes,anoBissexto)

