amount=float(input("Enter the amount: "))
Air=float(input("Enter annual interest rate in percent: "))
nrmonths=int(input("Enter the number of months: "))
i=1
finamount=0
while (i<=nrmonths):
    finamount=(amount+finamount)*(1+(Air/1200))
    i+=1
print("The amount in the savings after "+str(nrmonths)+" is: "+str("%.2f"%finamount))