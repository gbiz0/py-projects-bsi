cont = 0
vet = [0.0] * 5

for cont in range(0,5):
    vet[cont] = float(input(f"Inform a number for position {cont}: "))
for cont in range(5):
    print(f"[{vet[cont]}]", end = '')