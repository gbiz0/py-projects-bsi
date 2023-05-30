#faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 6 posições. 
#O usuário deverá inserir valores positivos e negativos. Substitua todas as ocorrência de valores positivos por 1 
# e todos os valores negativos por 0.

x = 0
vet = [0]*6

for x in range (0,6):
    vet[x] = int(input("Write a value: "))
    
print("Before trade: ", vet)

for x in range (6):
    if vet[x] >= 0:
        vet [x] = 1
        
    else:
        vet[x] = 0

print("After trade: ", vet)
        