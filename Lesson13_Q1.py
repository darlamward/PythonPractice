# A program to show the loan amount and repayment amount.
# Author: Darla Ward
# Date Completed: 05-24-2022

years = 1
interestRate = 0.065
loanAmount = float(input("Enter the loan amount: $"))
reason = input("Enter the reason for the loan: ")

while years <= 10:
    interest = loanAmount * interestRate * years
    repaymentAmount = loanAmount + interest
    monthlyPayment = repaymentAmount / (years * 12)
    print(years, loanAmount, repaymentAmount, monthlyPayment)
    years = years + 1
