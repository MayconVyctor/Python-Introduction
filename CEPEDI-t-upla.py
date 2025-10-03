#Lista - mutavel

a = [10,20,30,40,50]

#insert(40,1) na posicao 40 o valor 1
#append(50) somente o elemnto add no final
#pop() - sem nenhumm valor ele retira ultimo, a nao ser que passe a posiçao
#remove(30) apaga o dado diretamente

#tupla - imutavel

b = (10,20,30,40,50)
print(b[1])

#b[1] = 11 - errado
#print(b[1])

c = list(b) #transformar a tupla em lista, e o c passa a ser uma lista com valores de b
print(c)

d = tuple(a) #transformar uma lista em tupla e d recebe os valores de a como uma tupla
print(d)

#fatiamento e fatiamento inverso

a = (10,20,30,40,50,60,70,80,90)
print(a[3:6])

print(a[:3])

b = a[:3]
print(b)

#Dicionario é uma estrutura de dados
#mapa = map

pessoa = {"nome":"Mike","idade":21, "peso":72, "casado":True}
print(pessoa)
print(pessoa["peso"])

pessoa["altura"] = 1.77
print(pessoa)

pessoa["peso"] = 70
print(pessoa)

if "idade" in pessoa:
    print("A idade de ", pessoa["nome"]," é", pessoa["idade"])
    pessoa["idade"]
    del pessoa["casado"]
    print(pessoa)

for chave, valor in pessoa.items():
    print(f"{chave} - {valor}")

