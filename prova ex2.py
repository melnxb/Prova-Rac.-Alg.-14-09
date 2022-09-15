idade = 65
tempoTrab = 30
idade2 = 60
tempoTrab2 = 25

print("Olá")
idad = float(input("Informe seu tempo de serviço: "))

trab = float(input("Informe sua idade: "))

if idad >= 65 and trab < tempoTrab:
    print("Você pode se aposentar.")
elif idad >= 65 and trab > tempoTrab:
    print("Você pode se aposentar.")

elif trab >= tempoTrab and idad <= 65:
    print("Você pode se aposentar.")
elif idad >= idade2 and trab >= tempoTrab2:
    print("Você pode se aposentar.")
else:
    print("Você não pode se aposentar")

