# Tip Calculator
print("Welcome to Tip Calculator")
billAmount = float(input("Enter The Bill Amount :\n"))
tipPercent = int(input("Enter the percentage of tip amount :\n"))
people = int(input("Enter the no. of people to share the bill :\n"))
totalAmount = billAmount + (billAmount / tipPercent)
finalBill = totalAmount / people
print("Amount you have to with tip : ${:.2f}".format(finalBill))
