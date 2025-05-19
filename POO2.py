# Aqui vai seu código
class Pessoa:
    def __init__(self, nome, anoNasc,documentoRG, nascionalidade):
        self.nome = nome
        self.anoNasc = anoNasc
        self.documentoRG = documentoRG
        self.nascionalidade = nascionalidade

pessoa1 = Pessoa("Mike", 2004, 1234, "Brasileiro")

class ContaBancaria:
    def __init__(self, titular, saldo, tipoDeConta, moeda):
        self.titular = titular 
        self.saldo = saldo
        self.tipoDeConta = tipoDeConta
        self.moeda = moeda

    def mostrarInformacoes(self):
       print(f"Titular Da Conta: {self.titular.nome}\nSaldo: {self.saldo}\nTipo De Conta: {self.tipoDeConta}\nMoeda: {self.moeda}")

conta1 = ContaBancaria(pessoa1, 1200, "Corrente", "Dolar" )
conta1.mostrarInformacoes()