# Aqui seu código
class CarroBrinquedo:
    def __init__(self, modelo, preco, cor):
      self.modelo = modelo
      self.preco = preco
      self.cor = cor

    def mostrarInformacoes(self):
        print(f"Modelo Do Produto: {self.modelo}\nPreço: {self.preco}\nCor: {self.cor}")

CarroMario = CarroBrinquedo("Carrinho do Mario", 299, "Vermelho\n")
ConversivelVerm = CarroBrinquedo("Conversivel", 250, "Vermelho\n")
CarroRally = CarroBrinquedo("Carro de Rally", 200, "Azul\n")
CarroRallyAberto = CarroBrinquedo("Carro de Rally aberto", 150, "Preto/Azul")

CarroMario.mostrarInformacoes()
ConversivelVerm.mostrarInformacoes()
CarroRally.mostrarInformacoes()
CarroRallyAberto.mostrarInformacoes()