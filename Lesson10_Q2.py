# A program that shows what's returned after paying for a purchase.
# Author: Darla Ward
# Date Completed: 05-19-2022

total = float(input("Enter the total of the purchase: $"))
payment = float(input("Enter the amount of the payment: $"))

change = int((payment - total) * 100)
twentyBills = "{:,.2f}".format(change // 2000)
change = change % 2000
tenBills = "{:,.2f}".format(change // 1000)
change = change % 1000
fiveBills = "{:,.2f}".format(change // 500)
change = change % 500
toonies = "{:,.2f}".format(change // 200)
change = change % 200
loonies = "{:,.2f}".format(change // 100)
change = change % 100
quarters = "{:,.2f}".format(change // 25)
change = change % 25
dimes = "{:,.2f}".format(change // 10)
change = change % 10
nickles = "{:,.2f}".format(change // 5)
change = change % 5
pennies = "{:,.2f}".format(change)

print("Twenty Dollar Bills:", twentyBills)
print("Ten Dollar Bills:   ", tenBills)
print("Five Dollar Bills:  ", fiveBills)
print("Toonies:            ", toonies)
print("Loonies:            ", loonies)
print("Quarters:           ", quarters)
print("Dimes:              ", dimes)
print("Nickles:            ", nickles)
print("Pennies:            ", pennies)