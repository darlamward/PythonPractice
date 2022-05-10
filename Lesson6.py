# Customer Confirmation for Holiday Plus.
# Author: Darla Ward
# Completion Date: 05-10-2022

location = "Disney California"
departure = "11-18-2023"
weeks = 4
customer = "Billie Bushell"
city = "St. John's"
street = "13 Trickall Avenue"
zipCode = "A7E3C1"
province = "NL"
holidayCost = 9999.99
HST = .15
downPayment = 4789.99

holidayHST = holidayCost * HST
totalDue = (holidayCost + holidayHST) - downPayment

holidayCost = "${:,.2f}".format(holidayCost)
holidayHST = "${:,.2f}".format(holidayHST)
downPayment = "${:,.2f}".format(downPayment)
totalDue = "${:,.2f}".format(totalDue)

print()
print("{:<73}".format("  HOLIDAY PLUS - CUSTOMER CONFIRMATION"))
print()
print("  Location: {:<20s}  Departure Date: {:<8s}   # weeks: {:<1d}".format(location, departure, weeks))
print()
print("  Customer:", " " * 33, "Charges:")
print()
print("  {:<24s}                    Holiday Cost:   {:<9s}".format(customer, holidayCost))
print("  {:<24s}                    Tax:            {:<9s}".format(street, holidayHST))
print("  {},{:<2s} {:<6s}                        Down Payment:   {:<9s}".format(city, province, zipCode, downPayment))
print("{:>71}".format("-" * 25))
print("{:>71}".format("Total Due:      {:<9s}".format(totalDue)))
print()
print("{:<71}".format("  Authorization: ___________________"))
print()
print("{:^73}".format("Thank you for booking with Holidays Plus Travel. Enjoy your trip."))
