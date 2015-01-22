# list of men and women from 0 to 99
men = [x for x in range (100)]
women = [x for x in range (100)]

# list of even numbered men to odd numbered women
eMen_oWomen = [('M:' + str(x), 'W:' + str(y)) for x in men if x % 2 == 0 for y in women if y % 2 == 1]

# list of odd numbered men to even numbered women
oMen_eWomen = [('M:' + str(x), 'W:' + str(y)) for x in men if x % 2 == 1 for y in women if y % 2 == 0]

# display 
print("Even # Men, Odd # Women")
print(eMen_oWomen)
print('\n')
print("Odd # Men, Even # Women")
print(oMen_eWomen)
