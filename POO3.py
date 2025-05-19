# Aqui seu código
class PessoaClinica:
    def __init__(self, nome, idade, tipoDeSangue, peso, altura):
        self.nome = nome
        self.idade = idade
        self.tipoDeSangue = tipoDeSangue
        self.peso = peso
        self.altura = altura

    def mostrarInformacoes(self):
      print(f"Nome: {self.nome}\nIdade: {self.idade}\nTipo De Sague: {self.tipoDeSangue}\nPeso: {self.peso}\nAltura: {self.altura}")

class PessoaEsoterica:
    def __init__(self, nome, idade, signoDoZodiaco, horarioNasc):
        self.nome = nome
        self.idade = idade
        self.signoDoZodiaco = signoDoZodiaco
        self.horarioNasc = horarioNasc

    def mostrarInformacoes(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nSigno Do Zodiaco: {self.signoDoZodiaco}\nHorario Nascimento: {self.horarioNasc}\n")

class PessoaRedeSocial:
    def __init__(self, nome, idade, corDosOlhos, hobbies, altura):
        self.nome = nome
        self.idade = idade
        self.corDosOlhos = corDosOlhos
        self.hobbies = hobbies
        self.altura = altura
    
    def mostrarInformacoes(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nCor Dos Olhos: {self.corDosOlhos}\nHobbies: {self.hobbies}\nAltura: {self.altura}")


Alex = PessoaClinica("Alex", 21, "O-", "80kg", "1.76m\n")
Maria = PessoaEsoterica("Maria", 21, "Peixes", "7:30h\n")
Jonas = PessoaRedeSocial("Jonas", 21, "Castanho Escuro", "Jogar Videogame", "1.77m")

Alex.mostrarInformacoes()
Maria.mostrarInformacoes()
Jonas.mostrarInformacoes()