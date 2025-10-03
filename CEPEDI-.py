def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

while True:
    print(" ---------------- ")
    print("1- Soma")
    print("2- Subtrair")
    print("3- Sair")
    print()

    opcao = int(input("Escolha: "))
    if opcao == 1:
        num1= int(input("Digite os valores do primeiro termo: "))
        num2 = int(input("Digite os valores do segundo termo: "))
        soma(num1, num2)
        print(soma(num1, num2))

    elif opcao == 2:
        num1 = int(input("Digite os valores do primeiro termo: "))
        num2 = int(input("Digite os valores do segundo termo: "))
        subtrair(num1, num2)

    elif opcao == 3:
        break