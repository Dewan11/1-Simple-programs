gross_salary = float(input("Enter gross salary: "))

allowances = 0.1 * gross_salary
deductions = 0.03 * gross_salary

net_salary = gross_salary + allowances - deductions

print("Net salary is", net_salary)