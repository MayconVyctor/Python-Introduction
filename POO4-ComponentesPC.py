class Componente:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def mostrarInformacoes(self):
        print(f"Tipo: {self.tipo}\nMarca: {self.marca}\nModelo: {self.modelo}")

Componente1 = Componente("RAM", "Asgard", "DDR4\n")

class Computador:
    def __init__(self, componentes):
        self.componentes = []

    def adicionarComponente(self, componente):
      if isinstance(componente, Componente):
        self.componentes.append(componente)
      else:
        print("Componente invalido")

    def exibirComponentes(self):
        for componente in self.componentes:
          componente.mostrarInformacoes()

    def removerComponente(self, componente):
       self.componentes.remove(componente)


Componente2 = Componente("SSD", "Kingston", "NVMI\n")
Componente3 = Componente("Processador", "intel", "i999k\n")

Computador1 = Computador([])

Computador1.adicionarComponente(Componente1)
Computador1.adicionarComponente(Componente2)
Computador1.adicionarComponente(Componente3)


#Computador1.removerComponente(Componente2)
Computador1.exibirComponentes()