pessoa = {}

for info in range (1,2):
    pessoa["nome"] = input("Digite o  seu nome: ")
    pessoa["idade"] = int(input("Digite sua idade: "))
    print(pessoa)
    pessoa["peso"] = float(input("Digite sua peso: "))

print(pessoa)
