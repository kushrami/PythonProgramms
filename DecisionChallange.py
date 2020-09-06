UserCountry = input("Please enter your country name here : ")
TotalOrder = float(input("Please Enter your total amount of order : "))

if UserCountry.upper() == "INDIA":
    UserProvince = input("Please enter your province : ")
    Anytaxes = True
else :
    Anytaxes = False
CalculatedTax = 0.0
if Anytaxes == True:
    if UserProvince == "Delhi":
        CalculatedTax = TotalOrder * 0.05 / 100.0
    elif UserProvince == "Gujarat" or UserProvince == "Andra" or UserProvince == "Mumbai":
        CalculatedTax = TotalOrder * 0.13 / 100.0
    else :
        CalculatedTax = (TotalOrder * 0.06/100.0) + (TotalOrder * 0.05/100.0)
else :
    CalculatedTax = (TotalOrder * 0.06/100.0) + (TotalOrder * 0.05/100.0)

print("Your Total Charge is : ",float(TotalOrder) + CalculatedTax)