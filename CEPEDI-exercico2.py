#Crie um algoritmo que leia 2 valores e escreva na tela a media ponderada entre eles. priemiro valor 40% e segundo peso 60%

num1 = int(input("Insira um numero: "))
num2 = int(input("Insira um numero: "))
mediaPonderada = (num1*0.40 + num2*0.60)

print(mediaPonderada)