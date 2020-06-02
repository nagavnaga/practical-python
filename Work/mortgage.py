# mortgage.py
#
# Exercise 1.7
"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000
with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation.
The interest rate is 5% and the monthly payment is $2684.11.
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108
table = '{:6}| {:<11}| {}'

print(table.format("Month", "Total_paid", "Remaining_principal"))
while principal > 0 and principal > payment:
    month = month + 1
    principal = principal * (1 + rate / 12) - payment

    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        # if extra_payment_end_month >= month >= extra_payment_start_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    # print(table.format(month, round(total_paid,2), round(principal, 2)))
    print(f'{month:<6}| {total_paid:<11.2f}| {principal:0.2f}')
# print('Months paid', month)
# print('Total paid', total_paid)
