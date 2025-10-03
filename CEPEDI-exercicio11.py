#criar uma lista de qualquer coisa, como frutas,
# colocar elementos repetidos remover um destes elementos
# repetidos com revome e entender esse comportamento

jogos = ["The last of us","Hollow Knight", "The last of us", "inFamous", "The last of us", "The last of us", "inFamous"]
jogosRemovidos = 0
contadorDeJogosRemovidos = 0

for jogo in jogos:
     jogos.remove("The last of us")
     jogos.remove("inFamous")
     jogosRemovidos +1
     contadorDeJogosRemovidos +1
     if contadorDeJogosRemovidos != jogosRemovidos:
           break
print(jogos)
