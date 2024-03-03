# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months = months + 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        x = 1
    else: 
        x = 0
    principal = principal * (1+rate/12) - payment - extra_payment*x
    total_paid = total_paid + payment + extra_payment*x
    
    print(months, total_paid, principal)
    if principal < (payment + extra_payment*x):
        total_paid = total_paid + principal
        principal = 0
        months = months + 1
        print(months, total_paid, principal)
        break 

print(f'${total_paid:0.1f} paid in total during {months} months')


