from random import choice
from string import digits
user = str(input())
code = list(user)
for i in range(6):
    code.append(choice(digits))

print (''.join(code))