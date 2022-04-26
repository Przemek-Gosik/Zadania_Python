from math import *
print("(0 -single filers,1-married filing jointly,\n 2-married filing separately,3 -head ofhousehold)")
status=int(input("Enter the filing status: "))
tax=0
if (status == 0):
    taxableIncome = int(input("Enter the taxable income: "))
    a=8350
    b=33950
    c=82250
    d=171550
    e=372950
elif (status == 1):
    taxableIncome = float(input("Enter the taxable income: "))
    a=16700
    b=67900
    c=137050
    d=208850
    e=327950
    print("Tax is " + str(tax))
elif (status == 2):
    taxableIncome = float(input("Enter the taxable income: "))
    a=8350
    b=33950
    c=68525
    d=104425
    e=186475
elif (status == 3):
    taxableIncome = float(input("Enter the taxable income: "))
    a=11950
    b=45500
    c=117450
    d=190200
    e=372950
else:
    print("Wrong status!")
if(status >=0 and status<=3):
    while taxableIncome > a:
        if taxableIncome > e:
            tax=tax+((taxableIncome-e)*0.35)
            taxableIncome=e
        elif taxableIncome > d:
            tax=tax+((taxableIncome-d)*0.33)
            taxableIncome=d
        elif taxableIncome >c:
            tax=tax+((taxableIncome-c)*0.28)
            taxableIncome=c
        elif taxableIncome > b:
            tax=tax+((taxableIncome-b)*0.25)
            taxableIncome=b
        else:
            tax=tax+((taxableIncome-a)*0.15)
            taxableIncome=a
    tax=tax+(taxableIncome)*0.1
    print("Tax is " + str("%.2f"%tax))






