Employee = input("Enter Employee Name: ")
TripLoc = input("Enter Location of Trip: ")
NumofDays = int(input("Enter the number of days: "))  # defining as integer
NumofKM = int(input("Enter the number of KM: "))  # defining as integer

FoodAccCost = 56.00 * NumofDays # Decimals automatically makes the output a float
LodgingCost = 125.00 * NumofDays
KMCost = .24 * NumofKM

TotalCost = FoodAccCost + LodgingCost + KMCost

print("Employee Name: $", Employee)
print("Location of Trip: $", TripLoc)
print("Number of Days: $", NumofDays)
print("Number of Kilometers: $", NumofKM)
print("Total claim for Food and Accidentals: ${:.2f}".format(FoodAccCost)) # {:.2f}".format(xxxxx) makes it read 2 decimal places
print("Total claim for Lodging: ${:.2f}".format(LodgingCost))
print("Total claim for Mileage: ${:.2f}".format(KMCost))
print("Total claim for the entire trip: ${:.2f}".format(TotalCost))