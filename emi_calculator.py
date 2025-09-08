
# Developed a Python-based EMI Calculator with loan eligibility checks and multi-year repayment 
# comparisons to help car buyers estimate monthly payments and total costs.

#### Case 1: User submits information on down payment
on_road_price = 2500000
down_payment = int(input("Enter down payment: "))

if down_payment >= on_road_price:
    print("Your down payment can't be greater than or equal to your road price.")
    exit()

# Code calculates loan amount
loan_amount = on_road_price - down_payment

# Annual interest rate fixed to 8%
annual_interest_rate = 0.08 #interest rate applied on on_road_price
monthly_interest_rate = annual_interest_rate / 12

# Loan period input captured from user in years and converted to months
loan_period = int(input("Select Loan Period (1-7) years: "))
months = loan_period * 12

# EMI calculated below:
EMI = (loan_amount * monthly_interest_rate * (1+monthly_interest_rate) ** months)/ (((1+monthly_interest_rate) ** months) - 1)
interest_compound = (1+monthly_interest_rate)**months

payable_amount = EMI * months
print(f"Payable Amount is {payable_amount:,.2f}")
print(f"Monthly EMI: {EMI:,.2f}")


#### Case 2: Code block adjusted for (1) loan eligiblity requirement, (2) prepayment option and (3) multi-year EMI comparisons
on_road_price = 2108771
down_payment = int(input("Enter down payment: "))

if down_payment >= on_road_price:
    print("Your down payment can't be greater than or equal to your road price.")
    exit()

loan_amount = on_road_price - down_payment
max_loan_ratio = 0.85  # bank allows 80% loan

if loan_amount > on_road_price * max_loan_ratio:
    print("Loan amount exceeds loan amount that can be provided. Please re-enter a higher down payment.")
else:
    print("Your EMI breakdowns can be found below.")

annual_interest_rate = 0.08
monthly_interest_rate = annual_interest_rate / 12

# Via this code, user can compare multiple loan periods (36, 60 and 84 months / 3,5,7 years)
loan_periods = [3, 5, 7]
for period in loan_periods:
    months = period * 12
    EMI = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / \
          ((1 + monthly_interest_rate) ** months - 1)
    total = EMI * months

    print(f"\nFor {period} years:")
    print(f"  Monthly EMI: ₹{EMI:,.2f}")
    print(f"  Total payable: ₹{total:,.2f}")