# Calculating Compound Interest
# By Ronald Tejada

# A = P(1 + r/n)^nt
# P = principal amount (initial investment)
# r = annual nominal interest rate (as a decimal)
# n = number of times the interest is compounded per year
# t = number of years

p = float(input("How much money will you initially invest? "))
n = int(input("How many times a year will the interest be compounded? "))
r = float(input("What is the nominal interest rate? "))

print("An amount of $", p, " will be compounded ", n, " times a year at an interest rate of ", r, "%.")

t = int(input("How many months do you want this amount to be compounded for? "))

# Converting the annual nominal interest to a decimal
r = r/100

# Converting months to years
t = t/12

a = p*(1 + r/n)**(n*t)
print("The total amount is $", a, ".")
print("The interest amount is $", a - p, ".")
