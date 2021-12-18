user = input("Enter a word: ")
lenght = len(user)
if lenght == 0:
    print("0000")
elif lenght == 1:
    print(user*4)
elif lenght == 2:
    print(user*2)
else:
    ans = user[1]+user[0]+user[-1]+user[-2]
    print(ans)