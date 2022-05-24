# A program to process customer statements for electricity used in a month.
# Author: Darla Ward
# in progress

lessRate = 7.30
overRate = 6.90
lessDiscountRate = 0.01
overDiscountRate = 0.03
HSTRate = 0.15

name = input("Enter Customer Name: ").upper()
streetAddress = input("Enter Street Address: ").upper()
previousReading = int(input("Enter the meter reading for the previous month: "))
currentReading = int(input("Enter the meter reading for this month: "))

hoursUsed = currentReading - previousReading

if hoursUsed <= 100:
    charge = hoursUsed * lessRate
else:
    charge = hoursUsed * overRate
if charge <= 500.00:
    discount = charge * lessDiscountRate
else:
    discount = charge * overDiscountRate
discountedSubtotal = charge - discount
discountedHSTCharge = discountedSubtotal * HSTRate
discountedTotalCharge = discountedSubtotal + discountedHSTCharge
subtotal = charge
HSTCharge = subtotal * HSTRate
totalCharge = subtotal + HSTCharge

print()
print()
print("{:^50}".format("NL Power Company"))
print("{:^50}".format("-" * 40))
print("{:<50}".format("Customer Statement for"), name)

