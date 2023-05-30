#Uma escola está realizando matrículas para um curso aberto à comunidade,
#com limite de 20 vagas. Assumindo que os alunos são cadastrados por computador,
#escreva um algoritmo que:
#Leia a idade e o sexo do aluno;
#Informe que a turma está lotada, quando o número de inscritos atingir a quantidade de vagas;
#Mostre a idade média dos candidatos;
#Mostre a quantidade de mulheres inscritas;
#Mostre os candidatos (homens e mulheres) maiores de idade.

age = 0
sex = ""
mean = 0
woman = ""
man = ""
cont = 0
max_age = 0
sum = 0

age = int(input("Inform your age: "))
sex = input("Inform your sex (M or F): ")

for cont in range(20):
    if (sex.upper == "F"):
        woman += 1
    if (age >= 18):
        max_age += 1
    
    sum += age
    
mean = sum / 20

print(f"The age mean of peoples:  {mean}")
print(f"Amont of woman: {woman}")
print(f"Amont of legal age: {max_age}")
        