class Jovens:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade


    def cidadeAtual(self):
      print(f"{self.nome} mora em {self.cidade}")

    def anoDeNascimento(self):
      nascimento = 2025 - self.idade
      print(self.nome, "nasceu no ano de", nascimento)

nomeJovem = input("informe o nome do jovem: ")
idadeJovem = int(input("Informe a idade do jovem: "))
cidadeDoJovem = input("informe a cidade do jovem: ")



mike = Jovens(nomeJovem, idadeJovem, cidadeDoJovem)
mike.cidadeAtual()
mike.anoDeNascimento()