#Foi feita uma pesquisa de audiência de canal de TV
#em várias casas de uma certa cidade, num determinado dia.
#    Para cada casa visitada, é fornecido o número do canal (9, 12, 23 ou 40).
#    Fazer um algoritmo que:
#       - leia um número indeterminado de dados,
#         até que seja digitado o canal 0(zero);
#       - Calcule e mostre a porcentagem de
#         audiência de cada emissora;
#       - Caso seja digitado algum canal fora dos
#         apresentado acima, informar como outros canais;
#       - O número 0(zero) não pode ser considerado um canal.

chanel = 0
cont = 0
chanel_9 = 0
chanel_12 = 0
chanel_23 = 0
chanel_40 = 0
m9 = 0
m12 = 0
m23 = 0
m40 = 0
m_other = 0
other = 0

chanel = int(input("Inform the chanel: ")) 

while (chanel != 0):
    
    chanel = int(input("Inform the chanel: "))
    
    if(chanel == 9):
        chanel_9 += 1
        cont += 1
    elif (chanel == 12):
        chanel_12 += 1
        cont += 1
    elif(chanel == 23):
        chanel_23 += 1
        cont += 1
    elif (chanel == 40):
        chanel_40 += 1
        cont += 1
    else:
        other += 1
        cont += 1
    
if (cont != 0):
    m9 = (chanel_9 * 100) / cont 
    m12 = (chanel_12 * 100) / cont 
    m23 = (chanel_23 * 100) / cont 
    m40 = (chanel_40 * 100) / cont 
    m_other = (other * 100) / cont 
        
print(f"The mean of chanel 9 is: {m9}%")
print(f"The mean of chanel 12 is: {m12}%")
print(f"The mean of chanel 23 is: {m23}%")
print(f"The mean of chanel 40 is: {m40}%")
print(f"The mean of other chanel is: {m_other}%")

    