def computeTax(status, taxableIncome):
    tax = 0
    if (status == 0):
        a = 8350
        b = 33950
        c = 82250
        d = 171550
        e = 372950
    elif (status == 1):
        a = 16700
        b = 67900
        c = 137050
        d = 208850
        e = 327950
    elif (status == 2):
        a = 8350
        b = 33950
        c = 68525
        d = 104425
        e = 186475
    elif (status == 3):
        a = 11950
        b = 45500
        c = 117450
        d = 190200
        e = 372950
    while taxableIncome > a:
        if taxableIncome > e:
            tax = tax + ((taxableIncome - e) * 0.35)
            taxableIncome = e
        elif taxableIncome > d:
            tax = tax + ((taxableIncome - d) * 0.33)
            taxableIncome = d
        elif taxableIncome > c:
             tax = tax + ((taxableIncome - c) * 0.28)
             taxableIncome = c
        elif taxableIncome > b:
            tax = tax + ((taxableIncome - b) * 0.25)
            taxableIncome = b
        else:
            tax = tax + ((taxableIncome - a) * 0.15)
            taxableIncome = a
    tax = tax + (taxableIncome) * 0.1
    return tax
print('{:<15s}{:>8s}{:>16s}{:>20s}{:>15s}'.format("Taxable income","Single","Married joint" ,"Married separate" ,"Head of house" ))
for i in range(50000 ,60050,50):
    tax1=computeTax(0,i)
    tax2=computeTax(1,i)
    tax3=computeTax(2,i)
    tax4=computeTax(3,i)
    print('{:<15s}{:>8s}{:>12s}{:>18s}{:>15s}'.format(str(i),str("%.0f"%tax1),str("%.0f"%tax2),str("%.0f"%tax3),str("%.0f"%tax4)))
