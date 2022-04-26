from math import *
loanAmount=int(input("Loan amount: "))
nryears=int(input("Number of years: "))
print('{:<15}{:^15}{:>15}'.format("Interest rate ","Monthly table","Total payment"))
i=0.05
while (i<0.08125):
    MonP = ((loanAmount*(i/12))/(1-1/(pow(1+(i/12),(nryears*12)))))
    ToP=MonP*nryears*12
    print('{:<15}{:^15}{:>15}'.format(str("%.3f"%(i*100))+"%",str("%.2f"%MonP),str("%.2f"%ToP)))
    i=i+0.00125


