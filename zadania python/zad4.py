Fav=int(input("Enter final account value: "))
Air=float(input("Enter annual interest rate in percent: "))
nryears=int(input("Enter number of years: "))
iDA=Fav/(pow(1+(Air/(12*100)),nryears*12))
print("Initial deposit value is "+ str(iDA))