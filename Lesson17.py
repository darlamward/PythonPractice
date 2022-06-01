# A program to determine if a credit card has a valid expiry date.
# Author: Darla Ward
# Date Completed: 06-01-2022
'''
The expiry date of a credit card is entered as MM/YY.  Ensure the middle character  is  a  /,
the  first  two  characters  are  between  01  and  12,
and  the  last  2 characters are within 4 years of the current year.
'''

import datetime

currentTime = datetime.datetime.now()
currentMonth = str(currentTime.month)
month = currentMonth[0:2]
currentYear = str(currentTime.year)
year = currentYear[2:4]

while True:
    expiry = input("Enter Credit Card Expiry Date (MM/YY):")

    if len(expiry) > 5:
        print("Date is too long.")
        break
    elif expiry[2] != "/":
        print("Date needs to be format MM/YY.")
        break
    elif int(expiry[0:2]) < 1 or int(expiry[0:2]) > 12:
        print("Not a valid month. Month needs to be between 01 and 12.")
        break
    elif int(expiry[3:5]) < int(year) or int(expiry[3:5]) > (int(year) + 4):
        print("Not a valid year. Year must be within 4 years of current year.")
        break
    elif int(expiry[0:2]) == int(month) and int(expiry[3:5]) == int(year):
        print("Your card expires this month.")
        print(expiry)
        break
    else:
        print("This is a valid expiry date.")
        print(expiry)
    break
