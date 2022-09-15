##Escreva um programa que apresente quatro opções: (1) consulta saldo, 
# (2) saque e (3) depósito e (4) sair. O saldo deve iniciar em R$ 0,00. A 
#cada saque ou depósito o valor do saldo deve ser atualizado. 
saldo = 1
saque = 2
deposito =3
sair = 4

saldoDin = 0
saque = 0
dinheiro = 0
deposito1 = saldo + dinheiro


print ("Bem-vindo, o que deseja fazer:")
print("1-Consultar saldo\n2-Saque\n3-Depósito\n4-Sair")


atividade = int(input("Digite o número da opção desejada: "))
if atividade == 1:
    print("R$" + str(float(saldoDin)))

elif atividade == 2:
    saque = float(input("Informe qual valor você deseja sacar: "))
    saldoDin = saldo - saque
    print("Saldo final:" + "R$" + str(saldoDin))

elif atividade == 3:
    dinheiro = float(input("Quanto deseja depósitar: "))
    saldoDin = saldo + dinheiro
    print("Seu saldo agora é de: " + "R$" + str(saldoDin))


else :
    print("Obrigado, volte sempre!")


