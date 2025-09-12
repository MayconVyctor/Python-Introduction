#Crie um algoritmo que leia o nome de um aluno, as notas de suas tres provas e calcule e exiba na tela a media harmonica das provas

nomeAlumo = input("Nome do aluno: ")
notaProva1 = int(input("Sua Nota na prova 1: "))
notaProva2 = int(input("Sua Nota na prova 2: "))
notaProva3 = int(input("Sua Nota na prova 3: "))

mediaHarmonica =  3 / ((1/ notaProva1 ) + (1/ notaProva2) + (1/ notaProva3))
print(mediaHarmonica)