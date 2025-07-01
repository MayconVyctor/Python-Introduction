class Abobora:
    def __init__(self, tamanho, forma, design):
        self.tamanho = tamanho
        self.forma = forma
        self.design = design

    def exibirDadosAbobora(self):
      print(f"Tamanho Abobora: {self.tamanho}\nFormato da Abobora: {self.forma}\nDesign da Abobora: {self.design}\n")

class Artesao:
    def __init__(self, nome, abobora):
        self.nome = nome
        self.abobora = abobora


    def exibirDadosArtesao(self):
         print(f"Nome do artesão: {self.nome}\nTrabalha com Abobora de Tamanho: {self.abobora.tamanho}\nTrabalha com Formato da Abobora: {self.abobora.forma}\nTrabalha com Design da Abobora: {self.abobora.design}\n")


class FabricaAboboras:
    def __init__(self):
        self.aboboras = []
        self.artesaos = []

    def adicionarAbobora(self, abobora):
        self.aboboras.append(abobora)

    def adicionarArtesao(self, artesao):
        self.artesaos.append(artesao)

    def mostrarCatalogo(self):
        for abobora in self.aboboras:
          abobora.exibirDadosAbobora()

    def relacionarArtesao(self, nome_artesao, tamanho_trabalhado, tamanho_abobora, formato_trabalhado, formato_abobora, design_trabalhado, design_abobora ):
        encontrado = False
        for abobora in self.aboboras:
          if nome_artesao == artesao.nome and tamanho_trabalhado == tamanho_abobora and formato_trabalhado == formato_abobora and design_trabalhado == design_abobora:
           artesao.exibirDadosArtesao()
           encontrado = True

          if not encontrado:
            print(f"Nenhuma Abobora para o {nome_artesao}")

sistema = FabricaAboboras()

while True:
     print("\n--- MENU ---")
     print("1. Adicionar Abobora")
     print("2. Adicionar Artesão")
     print("3. Mostrar catálogo")
     print("4. Relacionar Artesão")
     print("5. Sair")

     opcao = input("\nEscolha uma opção: ")

     if opcao == "1":
        tamanho_abobora = input("Informe o tamanho da Abobora: ")
        formato_abobora = input("Informe o formato da Abobora: ")
        design_abobora = input("Informe o desgin da Abobora: ")

        abobora = Abobora(tamanho_abobora, formato_abobora, design_abobora)
        sistema.adicionarAbobora(abobora)
        print("Abobora adicionada com sucesso!")

     elif opcao == "2":
       nome_artesao = input("Informe o nome do Artesao: ")
       tamanho_trabalhado = input("Informe o tamanho de abobora trabalhado: ")
       formato_trabalhado = input("Informe o formato de abobora trabalhado: ")
       design_trabalhado = input("Informe o design de abobora trabalhado: ")

       artesao = Artesao(nome_artesao, abobora)
       sistema.adicionarArtesao(artesao)
       print("Artesão adicionado com sucesso!")

     elif opcao == "3":
       sistema.mostrarCatalogo()

     elif opcao == "4":
       nome_artesao = input("\nDigite o nome do artesao para relacionar: ")
       sistema.relacionarArtesao(nome_artesao, tamanho_trabalhado, tamanho_abobora, formato_trabalhado, formato_abobora, design_trabalhado, design_abobora)

     elif opcao == "5":
        print("Encerrando o sistema...")
        break

     else:
        print("Opção inválida. Tente novamente.")