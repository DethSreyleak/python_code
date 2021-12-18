user = str(input("Enter Something: "))
reversed_name =''.join(reversed(user)) #join() method merges all of the characters resulting from the reversed iteration into a new string
if user == "":
    print("Nothing Not Display.")
else:
    print(reversed_name)
