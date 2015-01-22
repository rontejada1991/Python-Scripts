# Calculating Compound Interest
# By Ronald Tejada

# A = P(1 + r/n)^nt
# P = principal amount (initial investment)
# r = annual nomical interest rate (as a decimal)
# n = number of times the interest is compounded per year
# t = number of years

p = 10000
n = 12
r = 8
print("An amount of $", p, " will be compounded ", n, " times a year at an interest rate of ", r, "%.")

t = input("How many months do you want this amount to be compounded for? ")

# Converting 8% to a float to keep the decimal
r = float(r)/100

# Converting 't' months into years to fit our formula
t = int(t)/12

a = p*(1 + r/n)**(n*t)
print("The total amount is $", a, ".")
print("The interest amount is $", a - p, ".")
