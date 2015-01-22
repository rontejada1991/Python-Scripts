# 4.7.1

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('uncooperative user')
        print(complaint)

# This one simply asks a question
print(ask_ok('Do you like the beatles? '))

# This one asks a question and sets the retries to 2
print(ask_ok('Do you want to delete the multiverse? ', 2))

# This one does the previous two and changes the complaint
print(ask_ok('Are you high? ', 3, 'Dude, you are totally high'))

print()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print()

def f_non_subsequent(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f_non_subsequent(1))
print(f_non_subsequent(2))
print(f_non_subsequent(3))
