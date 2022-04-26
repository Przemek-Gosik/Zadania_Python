from math import *
InvA=float(input("Enter investment value: "))
Air=float(input("Enter annual interest rate in percent: "))
nryears=int(input("Enter number of years: "))
Acv=InvA*(pow(1+(Air/(12*100)),12*nryears))
print("Accumulated value is "+str("%.2f"%Acv))