# monthlyPayment = 0
# annualInterestRate = 0.2
# monthlyInterestRate = annualInterestRate /12
# balance = 3329
# newbalance = balance
# month = 0

# while newbalance > 0:
#     monthlyPayment += 10
#     newbalance = balance
#     for month in range(1,13):
#         newbalance -= monthlyPayment
#         newbalance += monthlyInterestRate * newbalance
#         month += 1
#         print(monthlyPayment)
# print ("Lowest Payment: ", monthlyPayment)

monthlyPayment = 0
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate /12
balance = 3329
newbalance = balance
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1
    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        interest = monthlyInterestRate * newbalance
        newbalance += interest
        month += 1
    newbalance = round(newbalance,2)
print(monthlyPayment)