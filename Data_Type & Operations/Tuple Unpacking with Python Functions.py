# Tuple Unpacking with Python Functions

stock_prices=[('appl', 200),('GooG',400),('MSFT',100)]
print('')
for item in stock_prices:
    print(item)
print('')   
for ticker,price in stock_prices:
    print(ticker)

print('')
for ticker,price in stock_prices:
    print(price+(0.1*price))



work_hours = [('Abby',100),('Sally',400),('Cassie',800)]


def employee_check(work_hours):
    current_max = 0
    employee_om = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_om = employee
        else:
            pass

    return (employee_om, current_max)

item=employee_check(work_hours)
print(item)


    
