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

hourlyWageDsp = "${:,.2f}".format(hourlyPayRate)
regularPayDsp = "${:,.2f}".format(regularPay)
commissionDsp = "${:,.2f}".format(commission)
grossPayDsp = "${:,.2f}".format(grossPay)
incomeTaxOnPayDsp = "${:,.2f}".format(incomeTaxOnPay)
CPPOnPayDsp = "${:,.2f}".format(CPPOnPay)
EIOnPayDsp = "${:,.2f}".format(EIOnPay)
unionDuesDsp = "${:,.2f}".format(unionDues)
totalDeductionsDsp = "${:,.2f}".format(totalDeductions)
netPayDsp = "${:,.2f}".format(netPay)

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
                                                                            hourlyWageDsp))
print("Tuesday:   {:>3d}".format(widgetsProducedTuesday))
print("Wednesday: {:>3d}       Regular pay:  {:>9s}".format(widgetsProducedWednesday, regularPayDsp))
print("Thursday:  {:>3d}       Commission:   {:>9s}".format(widgetsProducedThursday, commissionDsp))
print("Friday:    {:>3d}       --------------------------------".format(widgetsProducedFriday))
print("--------------       Gross pay:             {:>9s}".format(grossPayDsp))
print("Total:    {:>4d}       Income tax:  {:>9s}".format(totalWidgetsProduced, incomeTaxOnPayDsp))
print("{:>53}".format("CPP:         {:>9s}          ".format(CPPOnPayDsp)))
print("{:>53}".format("EI:          {:>9s}          ".format(EIOnPayDsp)))
print("{:>53}".format("Union dues:  {:>9s}          ".format(unionDuesDsp)))
print("{:>53}".format("Total deductions:      {:>9s}".format(totalDeductionsDsp)))
print("{:>53}".format("--------------------------------"))
print("{:>53}".format("Net pay:               {:>9s}".format(netPayDsp)))
print("{:>53}".format("================================"))
