
import math

print("finance calculator program ready!")
print("enter either 'investment' or 'bond' ")
print("investment - to calculate the amount of interest you'll earn on your investment (simple and compund) interest")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Get user input for calculator selection. The .lower() method is used to convert the user input to lowercase.
calculator_choice = input("pick your option: ").lower()

# Investment calculator
if calculator_choice == "investment":
    # Get user input for investment calculator
    deposit = float(input("amount of money that you are depositing (£): "))
    interest_rate = float(input("the interest rate (%): ")) / 100
    years = float(input("the number of years you plan on investing: "))
    interest_type = input("the type of interest you want to calculate - 'simple' or 'compound': ").lower()

    # Calculate the interest based on the user input
    if interest_type == "simple":
        total = deposit * (1 + interest_rate * years)
    elif interest_type == "compound":
        total = deposit * math.pow((1 + interest_rate), years)

    # Output the result
    print(f"total investment will be worth £{round(total, 2)} after {years} years.")

# Bond calculator
elif calculator_choice == "bond":
    # Get user input for bond calculator
    present_value = float(input("value of the house (£): "))
    interest_rate = float(input("interest rate (%): ")) / 100
    months = int(input("number of months: "))

    # Calculate the monthly repayment based on the user input
    monthly_interest_rate = interest_rate / 12
    monthly_repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

    # Output the result
    print(f"monthly repayment will be £{round(monthly_repayment, 2)} over {months} months.")

# Invalid choice
else:
    print("Invalid choice. Enter either 'investment' or 'bond' ")