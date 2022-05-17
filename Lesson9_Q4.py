#  A program used to calculate the shipping cost of packages with a local shipping company.
#  Author: Darla Ward
#  Date Completed: 05-16-2022

KGRate = 1.15
localFee = 2.30
provinceFee = 6.90
countryFee = 10.35
otherFee = 24.95

weight = int(input("Enter the weight of the package in kilograms: "))
region = input("Enter the region(Local, Province, Country, or Other): ").upper()

packageCost = weight * KGRate

if region == "LOCAL":
    shippingCost = packageCost + localFee
elif region == "PROVINCE":
    shippingCost = packageCost + provinceFee
elif region == "COUNTRY":
    shippingCost = packageCost + countryFee
else:
    shippingCost = packageCost + otherFee

packageCostDsp = "${:,.2f}".format(packageCost)
shippingCostDsp = "${:,.2f}".format(shippingCost)
localFeeDsp = "${:,.2f}".format(localFee)
provinceFeeDsp = "${:,.2f}".format(provinceFee)
countryFeeDsp = "${:,.2f}".format(countryFee)
otherFeeDsp = "${:,.2f}".format(otherFee)

print()
print()
print("Weight of Package: ", weight)
print("Region: ", region)
print()
print("Cost of Package: ", packageCostDsp)
print("Region: ", region)
if region == "LOCAL":
    print("Region Fee: ", localFeeDsp)
elif region == "PROVINCE":
    print("Region Fee: ", provinceFeeDsp)
elif region == "COUNTRY":
    print("Region Fee: ", countryFeeDsp)
else:
    print("Region Fee: ", otherFeeDsp)
print("Total Shipping Cost: ", shippingCostDsp)



