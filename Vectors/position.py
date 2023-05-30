#crie um algoritmo que crie e leia um vetor com 6 posições e a partir disso faça: 
#    -percorra cada elemento do vetor fazendo:
#    -  se for um valor negativo, mostre o módulo (valor sem sinal) do valor; 
#    -  se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;
#   -  Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5.

vet = [0]*6

for cont in range(6):
    vet[cont] = int(input("Inform a number: "))

for cont in range(6):
    if (vet[cont] < 0):
        vet[cont] = vet[cont] * -1
    elif (vet[cont] > 10):
        vet[cont] = int(input("Inform a number: "))
        vet[cont] = vet[cont] - vet[cont]
    else:
        vet[cont] = vet[cont] / 5
        
print(vet)