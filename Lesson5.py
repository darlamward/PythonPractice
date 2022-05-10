# invoice for Honest Peter's Garage
# Author: Darla Ward
# Completion Date : 05-09-2022

invoiceNumber = "0028"
date = "05-09-22"
customer = "Saul Goodman"
plateNumber = "JXC 325"
street = "12 Juniper St."
mileage = 4572
city = "Port Hope Simpson"
province = "NL"
zip = "A1N 3B9"
costOfLabour = 367.00
costOfParts = 578.00
totalDiscount = 13.00
HST = .15
totalHST = HST * (costOfParts + costOfLabour)
invoiceTotal = (costOfParts + costOfLabour + totalHST) - totalDiscount
close = "Honest Peter's - There to meet the needs of our customer!!"

print("{:^70}".format("HONEST PETER'S GARAGE"))  # center on line
print("{:^70}".format("123 Fixit Street"))
print("{:^70}".format("St. John's, NL  A1A 1A1"))
print("  Invoice#: {:<4s}                                      Date: {:>8s}".format(invoiceNumber, date))  # invoice variable 4 spaces long and string, date variable 8 spaces long and string
print("{:^70}".format("-" * 66))  # center on page 66 * -
print("   Customer: {:<30s}    Plate Number: {:>6s}".format(customer, plateNumber))
print("   Address:  {:<30s}    Mileage:       {:>6d}".format(street, mileage))
print("             {:<18s}, {:<2s}  {:<6s}".format(city, province, zip))  # print multiple variables on one line
print()

costOfPartsDsp = "${:,.2f}".format(costOfParts)  # set up as currency
costOfLabourDsp = "${:,.2f}".format(costOfLabour)
totalDiscountDsp = "${:,.2f}".format(totalDiscount)
totalHSTDsp = "${:,.2f}".format(totalHST)
invoiceTotalDsp = "${:,.2f}".format(invoiceTotal)

print("{:>68}".format("Cost of Labor:  {:>9s}".format(costOfLabourDsp)))  # right align costOfLabourDsp for 68 spaces
print("{:>68}".format("Cost of Parts:  {:>9s}".format(costOfPartsDsp)))
print("{:>68}".format("Total Discount:  {:>9s}".format(totalDiscountDsp)))
print("{:>68}".format("-" * 9))
print("{:>68}".format("Invoice Total:  {:>9s}".format(invoiceTotalDsp)))
print("{:^70}".format("-" * 66))  # center
print("{:^70}".format(close))
print("{:^70}".format("-" * 66))
