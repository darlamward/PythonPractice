MonthlyRev = float(input("Enter Total Monthly Revenue: $"))
MortgageCost = float(input("Enter Monthly Mortgage Cost: $"))
FoodCost = float(input("Enter Monthly Grocery Cost: $"))
ClothingCost = float(input("Enter Monthly Clothing Cost: $"))
EntertainmentCost = float(input("Enter Monthly Entertainment Cost: $"))

TotalExpenses = MortgageCost + FoodCost + ClothingCost + EntertainmentCost
TotalSavings = MonthlyRev - TotalExpenses

MortgagePercent = MortgageCost/MonthlyRev * 100
FoodPercent = FoodCost/MonthlyRev * 100
ClothingPercent = ClothingCost/MonthlyRev * 100
EntertainmentPercent = EntertainmentCost/MonthlyRev * 100

print("Monthly Revenue:               $", MonthlyRev)
print("Monthly Mortgage Cost:         $", MortgageCost)
print("Monthly Cost of Groceries:     $", FoodCost)
print("Monthly Cost of CLothing:      $", ClothingCost)
print("Monthly Cost of Entertainment: $", EntertainmentCost)
print()
print("Total Expenses for the Month: ${:.2f}".format(TotalExpenses))
print("Total Savings for the Month:  ${:.2f}".format(TotalSavings))
print()
print("Percent of Revenue used for Mortgage Costs:      %", MortgagePercent)
print("Percent of Revenue used for Food Costs:          %", FoodPercent)
print("Percent of Revenue used for Clothing Costs:      %", ClothingPercent)
print("Percent of Revenue used for Entertainment Costs: %", EntertainmentPercent)