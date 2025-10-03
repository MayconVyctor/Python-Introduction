#faça um programa em python que gere um tabuleiro de xadrez simples em texto,
# usando laços aninhados, por exemplo,
# com # para representar as casas pretas e espaços para representar as casas brancas

for i in range (8):
    if i % 2 != 0:
     print("#  #  #  #  #")
    for j in range (8):
       if i % 2 == 0:
        print("  #  #  #  #  ")