# A employee payroll summary slip to display the calculations from the Widgets Inc. employee payroll program.
# Author: Darla Ward
# Date Completed : 05-11-2022

hourlyPayRate = 17.50
widgetCommissionRate = .35
incomeTaxRate = .21
CPPRate = 0.0495
EIRate = 0.016
unionDues = 15.00

employeeName = input("Enter employee name: ")
hoursWorked = int(input("Enter the amount of hours worked: "))
# widgets produced is between 200 & 500 per day
widgetsProducedMonday = int(input("Enter the number of widgets produced on Monday: "))
widgetsProducedTuesday = int(input("Enter the number of widgets produced on Tuesday: "))
widgetsProducedWednesday = int(input("Enter the number of widgets produced on Wednesday: "))
widgetsProducedThursday = int(input("Enter the number of widgets produced on Thursday: "))
widgetsProducedFriday = int(input("Enter the number of widgets produced on Friday: "))

totalWidgetsProduced = (widgetsProducedMonday + widgetsProducedTuesday + widgetsProducedWednesday
                        + widgetsProducedThursday + widgetsProducedFriday)
commission = totalWidgetsProduced * widgetCommissionRate
regularPay = hoursWorked * hourlyPayRate
grossPay = regularPay + commission

incomeTaxOnPay = grossPay * incomeTaxRate
CPPOnPay = grossPay * CPPRate
EIOnPay = grossPay * EIRate

totalDeductions = incomeTaxOnPay + CPPOnPay + EIOnPay + unionDues
netPay = grossPay - totalDeductions

hourlyWage = "${:,.2f}".format(hourlyPayRate)
regularPay = "${:,.2f}".format(regularPay)
commission = "${:,.2f}".format(commission)
grossPay = "${:,.2f}".format(grossPay)
incomeTaxOnPay = "${:,.2f}".format(incomeTaxOnPay)
CPPOnPay = "${:,.2f}".format(CPPOnPay)
EIOnPay = "${:,.2f}".format(EIOnPay)
unionDues = "${:,.2f}".format(unionDues)
totalDeductions = "${:,.2f}".format(totalDeductions)
netPay = "${:,.2f}".format(netPay)

print()
print()
print("{:<53}".format("Widgets Inc."))
print("{:<53}".format("Employee Payroll Summary"))
print()
print("{:<53}".format("Employee name: {:<18s}".format(employeeName)))
print()
print("{:<53}".format("Widgets produced:"))
print()
print("Monday:    {:>3d}       Hours worked: {:>2d}    Rate: {:>6s}".format(widgetsProducedMonday, hoursWorked,
                                                                            hourlyWage))
print("Tuesday:   {:>3d}".format(widgetsProducedTuesday))
print("Wednesday: {:>3d}       Regular pay:  {:>9s}".format(widgetsProducedWednesday, regularPay))
print("Thursday:  {:>3d}       Commission:   {:>9s}".format(widgetsProducedThursday, commission))
print("Friday:    {:>3d}       --------------------------------".format(widgetsProducedFriday))
print("--------------       Gross pay:             {:>9s}".format(grossPay))
print("Total:    {:>4d}       Income tax:  {:>9s}".format(totalWidgetsProduced, incomeTaxOnPay))
print("{:>53}".format("CPP:         {:>9s}          ".format(CPPOnPay)))
print("{:>53}".format("EI:          {:>9s}          ".format(EIOnPay)))
print("{:>53}".format("Union dues:  {:>9s}          ".format(unionDues)))
print("{:>53}".format("Total deductions:      {:>9s}".format(totalDeductions)))
print("{:>53}".format("--------------------------------"))
print("{:>53}".format("Net pay:               {:>9s}".format(netPay)))
print("{:>53}".format("================================"))
