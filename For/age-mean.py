#Construir um algoritmo que leia a idade de N pessoas. O sistema deve calcular: a média das idades, a menor e a maior idade informada

cont = 0
age = 0
sum = 0
mean = 0
n = 0
age_min = 0
age_max = 0

n = int(input("Inform the quant of peoples: "))

for cont in range (n):
    age = int(input("Inform the age: "))
    
    if (cont == 1):
        age_min == age
        age_max == age
    else:
        if (age > age_max):
            age_max = age
        elif (age < age_min):
            age_min = age
        
    sum = sum + age
    
mean = sum / n
    
print(f"The min age is:  {age_min}")
print(f"The mean age is: {mean}")
print(f"The max age is: {age_max}")
    
        

    

