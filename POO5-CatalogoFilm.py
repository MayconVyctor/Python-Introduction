class Filme:
    def __init__(self, titulo, classificacao):
        self.titulo = titulo
        self.classificacao = classificacao

    def mostrarFilmes(self):
       print(f"Titulo: {self.titulo}\nClassificação: {self.classificacao}\n")

Filme1 = Filme("Homem Aranha","Infatil/Ação" )

class Netflix:
    def __init__(self, filmes):
       self.filmes = []

    def adicionarFilme(self, filme):
        self.filmes.append(filme)

    def exibirFilmes(self):
        for filme in self.filmes:
            filme.mostrarFilmes()

Filme2 = Filme("Vingadores", "Ação")

Netflix1 = Netflix([])
Netflix1.adicionarFilme(Filme1)
Netflix1.adicionarFilme(Filme2)
Netflix1.exibirFilmes()