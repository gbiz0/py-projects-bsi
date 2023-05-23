price = float(input("Write the price of car: "))
proft = float(input("Write the proft of distributor (in percent): "))
tax = float(input("Write the tax of product (in percent): "))

Iproft = price * (proft/100)
Itax = price * (tax/100)
newprice = price + Iproft + Itax

print ("The proft is: $",Iproft)
print ("The tax is: $",Itax)
print ("The new price is: $",newprice)