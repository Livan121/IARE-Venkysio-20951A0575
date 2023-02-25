x = int(input("Gross salary per week:"))
a = float(input("federal deduction in %:"))
b = float(input("state deduction in %:"))
c = float(input("Company's pension plan in %:"))
w = int(input("No of weeks:"))
y = x*((a+b+c)/100)*w
z = x*w
print(z-y)