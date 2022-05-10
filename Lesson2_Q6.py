ItemName = input("Enter Item Name: ")
ItemCost = float(input("Enter Item Cost for Company: "))
NumOfStock = int(input("Enter Number of Stock for Item: "))


RetailPrice = ItemCost*1.75

TotalInvatCost = ItemCost * NumOfStock  # automatically read as a float because ItemCost is a float

TotalInvatRetail = RetailPrice * NumOfStock

GrossMargin = TotalInvatRetail - TotalInvatCost

SalesPrice10 = RetailPrice - (RetailPrice * .10)
SalesPrice25 = RetailPrice - (RetailPrice * .25)
SalesPrice33 = RetailPrice - (RetailPrice * (1/3))
SalesPrice50 = RetailPrice * .5


print("Item Name: ", ItemName)
print("Item Cost for Company: $ {:.2f}".format(ItemCost))
print("Number of Stock for Item: ", NumOfStock)

print("Retail Price: $ {:.2f}".format(RetailPrice))
print("Total Inventory at Cost: $ {:.2f}".format(TotalInvatCost))
print("Total Inventory at Retail: $ {:.2f}".format(TotalInvatRetail))
print("Gross Margin: $ {:.2f}".format(GrossMargin))

print("Sales Price at 10% off: $ {:.2f}".format(SalesPrice10))
print("Sales Price at 25% Off: $ {:.2f}".format(SalesPrice25))
print("Sales Price at 1/3% Off: $ {:.2f}".format(SalesPrice33))
print("Sales Price at 50% Off: $ {:.2f}".format(SalesPrice50))