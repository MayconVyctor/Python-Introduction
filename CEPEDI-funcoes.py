#Funções = Operações = Metodos = Procedimentos = Rotina

#math.sin(1) - calculo interno/ operaçao interna que retorna valor
#print() - funçao mais utilizada

#antigo padrao escreva_linha
#padrao moderno escrevaLinha

def escrevaLinha():
    linha = ("-" * 30)
    print(linha)
    return linha

def escrevaLinhas():
    print("----")

def esccrevaTracoPersonalizado(tamanho):
   traco = "-"*tamanho
   print(traco)
   return traco

print("antes")
retorno = esccrevaTracoPersonalizado(50)
print("depois")
esccrevaTracoPersonalizado(10)

