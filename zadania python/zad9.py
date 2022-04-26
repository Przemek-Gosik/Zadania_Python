amount=float(input("Enter the initial eposit amount: "))
yd=float(input("Enter annual percentage yield: "))
nrmonths=int(input("Enter maturity period (number of months): "))
print('{:<6s}{:>9s}'.format("Month","CD Value"))
for i in range(1,nrmonths+1):
    amount=amount+(amount*yd/1200)
    print('{:<6s}{:>9s}'.format(str(i),str("%.2f"%amount)))