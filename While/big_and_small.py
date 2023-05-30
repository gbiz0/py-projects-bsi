#Faça um algoritmo que solicite N números inteiros
#até que o número 0(zero) seja digitado.
#Ao final o algoritmo deve informar o maior e
#o menor número digitado.
#OBS: O número 0(zero) não pode ser contado.

n = 0
number = 0
cont = 0
min = 0
max = 0

number = int(input("Inform a number: "))
max == number
min == number

while (number != 0):
    if (number > max):
        max = number
    elif(number < min) & (number != 0):
        min = number
        
    number = int(input("Inform a number: "))
    
print(f"The max number is: {max}")
print(f"The min number is: {min}")

        