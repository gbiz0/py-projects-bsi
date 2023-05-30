#Construir um algoritmo que solicite um número e calcule a tabuada deste número
cont = 0
number = 0

number = int(input("Inform a number for multiplication table: "))

for cont in range(1,11):
    print(f"{number} x {cont} = {number * cont}")

