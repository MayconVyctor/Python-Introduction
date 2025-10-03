#listas
#array
#arranjo
#vetor

frutas = ["Morango", "Uva", "Amora", "Banana", "Manga"]
print(len(frutas))
print(frutas)

print(frutas[-1])
print(frutas[-2])

frutas.insert(1,"Abacate")
print(frutas)
print(frutas[1])

frutas.append("Blueberry")
print(frutas)

frutas.remove("Banana")
print(frutas)

frutas.pop(3)
mangas = frutas.pop(3)
print(frutas)
print(mangas)

del(frutas[3])
print(frutas)



#for fruta in frutas:
#   print(frutas[-1])


