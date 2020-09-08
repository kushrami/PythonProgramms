CostOfLoan = float(input("Please enter your cost of loan = "))
InterestRate = float(input("Please enter your loan interst rate = "))
NumberOfYears = float(input("Please enter Number of years you want a loan = "))
InterestRate = InterestRate / 100.0

MonthlyPayment = CostOfLoan * (InterestRate * (InterestRate + 1.0) * NumberOfYears) / ( (1.0 + InterestRate) * NumberOfYears - 1.0) 

print("Your Monthly Payment of loan is",MonthlyPayment)