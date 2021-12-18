user = str(input("Enter Something: "))
reversed_string = []
index = len(user)
while index > 0:
    reversed_string += user[index - 1]#save value of str[index - 1] in reversed_string
    index = index - 1#decrement index
    print(reversed_string)
else:    
    print("Nothing Not Display.")