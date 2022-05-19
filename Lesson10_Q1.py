# A program to determine retail cost and rounding to next .95.
# Author: Darla Ward
# Date Completed: 05-18-2022


markUp = 1.75  # 75% markup

itemCost = float(input("Enter the cost of the item: $"))

retailCost = round((itemCost * markUp), 2)
oneDecRetailCost = round(retailCost, 1)
roundedRetailCost = round(oneDecRetailCost)

if roundedRetailCost <= oneDecRetailCost:
    FinalRetailCost = roundedRetailCost + 0.95
else:
    FinalRetailCost = roundedRetailCost - .05

roundedRetailCostDsp = "${:,.2f}".format(roundedRetailCost)
retailCostDsp = "${:,.2f}".format(retailCost)
FinalRetailCostDsp = "${:,.2f}".format(FinalRetailCost)
oneDecRetailCostDsp = "${:,.2f}".format(oneDecRetailCost)

print()
print()
# print("Retail Cost bare: ", retailCostDsp)
# print("Retail Cost 1 Decimal: ", oneDecRetailCostDsp)
# print("Rounded cost of bare price: ", roundedRetailCostDsp)
print("Retail Cost of Item(to next .95): ", FinalRetailCostDsp)


