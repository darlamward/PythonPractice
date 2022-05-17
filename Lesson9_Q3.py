#  A program to calculate the price of a rental car with Edsel Car Rental Company.
#  Author: Darla Ward
#  Date Completed: 05-16-2022

rentalRate = 35.00
KMRate = .10
freeKM = 100  # 100 KM are free per rental
maxOdometer = 99999

numOfDays = int(input("Enter the number of days the car was rented: "))
beforeKM = int(input("Enter the number of kilometers before renting: "))
afterKM = int(input("Enter the number of kilometers upon return of rental: "))

if beforeKM > afterKM:
    if beforeKM == maxOdometer:
        totalKM = afterKM
    elif beforeKM > maxOdometer:
        beforeKM = maxOdometer
        totalKM = afterKM
    else:
        totalKM = (maxOdometer - beforeKM) + afterKM
elif beforeKM == afterKM:
    totalKM = (maxOdometer - beforeKM) + afterKM
else:
    totalKM = afterKM - beforeKM
if totalKM > freeKM:
    kmToCharge = totalKM - freeKM
    KMCharge = kmToCharge * KMRate
else:
    KMCharge = 0.00

KMChargeDsp = "${:,.2f}".format(KMCharge)

priceOfRental = rentalRate * numOfDays
totalRentalPrice = priceOfRental + KMCharge

priceOfRentalDsp = "${:,.2f}".format(priceOfRental)
totalRentalPriceDsp = "${:,.2f}".format(totalRentalPrice)

print()
print()
print("Number of days rented: ", numOfDays)
print("Odometer before renting: ", beforeKM)
print("Odometer upon return: ", afterKM)
print()
print("Kilometers travelled: ", totalKM)
if KMCharge > 0.00:
    print("Kilometers travelled fee: ", KMChargeDsp)
else:
    print("Kilometers travelled fee: No Fee for 100 KM travelled.")
print("Price of Rental Car: ", priceOfRentalDsp)
print("Total Price of Rental: ", totalRentalPriceDsp)
