principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period: "))

interest = (principal * rate * time) / 100

print("The interest is", interest)