from math import *
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return (investmentAmount * (pow(1 + (monthlyInterestRate / 100), 12 * years)))
investmentAmount=float(input("Enter investment amount: "))
annualInterestRate=float(input("Enter annual interest rate in percent: "))
print('{:<6s}{:>15s}'.format("Years","Future Value"))
for i in range(1,31):
    fIV=futureInvestmentValue(investmentAmount,annualInterestRate/12,i)
    print('{:<6s}{:^18s}'.format(str(i),str("%.2f"%fIV)))