#crie uma lista de livros (titulos como strings),
# peça ao usuario que insira 2 novos livros (coloque no fim e outro no inicio da lista),
# depois remova um livro especifico informado por ele

livros = ["Haikyuu"]

novoLivro1 = str(input("Informe um novo livro: "))
novoLivro2 = str(input("Informe um novo livro: "))
livros.append(novoLivro1)
livros.append(novoLivro2)

print(livros)
removerLivro = str(input("Digite livro para remover: "))

if removerLivro in livros:
    livros.remove(removerLivro)
print(livros)