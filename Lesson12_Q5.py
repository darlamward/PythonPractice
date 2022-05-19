# A pricing program for a Museum.
# Author: Darla Ward
# Date Completed: 05-19-2022

fullPriceTicket = 22.50

dayOfTrip = input("Enter the day of your trip: ").upper()
age = int(input("Enter your age: "))

halfTicket = fullPriceTicket / 2
discountOffTicket = fullPriceTicket * .25
quarterOffTicket = fullPriceTicket - discountOffTicket

fullPriceTicket = "${:,.2f}".format(fullPriceTicket)
halfTicket = "${:,.2f}".format(halfTicket)
discountOffTicket = "${:,.2f}".format(discountOffTicket)
quarterOffTicket = "${:,.2f}".format(quarterOffTicket)

if dayOfTrip == "MONDAY":
    print("We are closed on Monday.")
elif dayOfTrip == "TUESDAY" or dayOfTrip == "THURSDAY":
    if dayOfTrip == "THURSDAY" and (age <= 6 or age >= 65):
        print("Your admission is free today.")
    else:
        print("You get a 50% discount of ", halfTicket, " so admission price is ", halfTicket, ".")
elif dayOfTrip == "WEDNESDAY":
    if 20 >= age >= 13:
        print("You get a 25% discount of ", discountOffTicket, " so admission price is ", quarterOffTicket, ".")
    else:
        print("You pay full price of ", fullPriceTicket, ".")
elif dayOfTrip == "FRIDAY":
    print("You pay full price of ", fullPriceTicket, ".")
else:
    if 12 >= age >= 6:
        print("You get a 50% discount of ", halfTicket, " so admission price is ", halfTicket, ".")
    else:
        print("You pay full price of ", fullPriceTicket, ".")
