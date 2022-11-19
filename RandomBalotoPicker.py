import random

BalUsua = [2, 12, 21, 40, 43]
BalOpc = []
BalGan = []
Contador = 0
x = int

for i in range(1,44):
    BalOpc.append(i)

for i in range(1,6):
    x = random.choice(BalOpc)
    print(x)
    BalGan.append(x)
    BalOpc.remove(x)

#Acá se envía a organizar el vector que acabamos de armar para poderlos comparar

print(BalOpc)
print(BalGan)

if BalUsua == BalGan:
    print("Usted es muy makia mi perro")
else:
    print("No nea, no le meta más plata a eso")
