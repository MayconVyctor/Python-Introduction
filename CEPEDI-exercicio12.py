#1- criar um tupla com cinco nomes de fruta, sendo um deles repetido

frutas = ("Banana", "Manga", "Morango", "Banana", "Uva")
print(frutas)

#Contar quantas vezes banana aparece na tupla
frutas.count("Banana")
print(frutas.count("Banana"))

frutas.index("Morango")
print(frutas.index("Morango"))

print(frutas.index("Banana"))

idade = (18, 19, 20, 21)
print(idade*3)

print(max(idade))
print(min(idade))

print(max(frutas)) #baseia na tabela asc
print(min(frutas)) #baseia na tabela asc

conjunto = set(frutas) #conjunto nao tem repetido e nem ordem u
print(conjunto)

soma = sum(idade)  #soma todos os valores
print(soma)

print(sorted(frutas))
print(sorted(idade))
print(sorted(idade ,reverse=True))

#crie uma tupla com um unico elemento

frutasOne = ("morango")
print(frutasOne)

idadeAdulto = (18, 19, 20, 21)
idadeVelho = (60, 50)

idadeGeral = idadeAdulto + idadeVelho
print(idadeGeral)

#verifique se um valor existe dentro da tupla com o operador in (por exemplo verificar se 20 esta na tupla (10,20 ,30)

tupla = (10, 20, 30, 40)

if 20 in tupla:
    print(tupla)

print(30 in tupla)

tuplaParaList = list(tupla)

tuplaParaList.append(60)

voltaTupla = tuple(tuplaParaList)
print(voltaTupla)

#dada uma tupla de tuplas, por exemplo ((1,2), (3,4),(5,6)), crie uma lista com a soma de cada tupla interna (ex[3,7,11]).

tuplaDeTupla = ((1,2), (3,4),(5,6))

somaTuplaList = []

for elemento in tuplaDeTupla:
    somaTuplaList.append (sum(elemento))
    print(soma)

print(somaTuplaList)

#dado uma tupla, retornem o segundo mair elemento

tuplaSegundoMaior = (10, 20, 30, 40, 50, 60, 70, 80, 90)

listaSegundoMaior  = list(tuplaSegundoMaior)


"""""
print(tuplaDeTuplaDeSoma)

tuplaDeTuplaParaList = list(tuplaDeTupla)
"""""