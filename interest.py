def balanceCalculation(balance, annualInterestRate, monthlyPaymentRate):
    for n in range (1,13):
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        remainingBalance = round((balance - minimumMonthlyPayment) + (monthlyInterestRate * (balance - minimumMonthlyPayment)), 2)
        balance = remainingBalance
        n += 1
    return remainingBalance

balanceCalculation(42, 0.2, 0.04)


for n in range (1,13):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    remainingBalance = round((balance - minimumMonthlyPayment) + (monthlyInterestRate * (balance - minimumMonthlyPayment)), 2)
    balance = remainingBalance
    n += 1
print(remainingBalance)