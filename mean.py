print ("Welcome to the mean calculator")

name = input("Write your name: ")
n1 = int(input("Write your first note: "))
n2 = int(input("Write your second note: "))
n3 = int(input("Write your third note: "))
n4 = int(input("Write your fourth note: "))

mean = (n1 + n2 + n3 + n4) / 4

print(f"{name}, your mean was: {mean}")
#or print(name,", your mean was: ",mean)

if (mean >= 6):
    print ("Approved")
    
else:
    if (mean >= 4):
        print ("Recovery")
    
    else:
        print ("Reproved")