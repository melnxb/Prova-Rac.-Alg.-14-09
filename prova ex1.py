#Escreva um programa para ler 3 valores inteiros e escrever o maior 
#deles. Considere que o usuário não informará valores iguais.
print("Digite três números diferentes:")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O número " + str(num1) + " é maior")

if num2 > num1 and num2 > num3:
    print("O número " + str(num2) + " é maior")

if num3 > num2 and num3 > num1:
    print("O número " + str(num3) + " é maior")

else:
    print("Os números são iguais.")

