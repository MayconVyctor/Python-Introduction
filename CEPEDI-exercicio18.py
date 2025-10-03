#escreva um programa  que dado o titulo de um livro informado pelo usuario
# , exiba umma mensagem informando se o livro esta disponivel ou nao, ou se ele nao esta cadastrado
livros = ["haikyuu", "demon slayer", "jujutsu kaisen", "horimya"]
disponivel = [True, False, True, False]

while True:
    print("ESCOLHA")
    print("1 - Consultar Livros")
    print("2 - Cadastrar Livros")
    print("3 - Sair do Programa")
    entrada = int(input("Digite uma opcao: "))

    if entrada == 1:
        consultaLivro = input("Digite o nome do Livro: ")
        if consultaLivro in livros:
            print("Livro Disponivel")

        else:
            indice = livros.find(consultaLivro)
            print(indice)
            print("livro nao cadastrado")
    if entrada == 2:
        cadastraLivro = input("Digite o nome do Livro: ")
        livros.append(cadastraLivro)

    if entrada == 3:
        print("Programa encerrado")
        break

"""
posicao = -1

for i, livro in enumerate(livros):
    if livroBuscado.strip().lower() == livros.lower():
        posicao = i
        break
if posicao == -1:
print("Livro nao cadastrado")
elif disponivel[posicao] == True:
print("Livro cadastrado")

"""