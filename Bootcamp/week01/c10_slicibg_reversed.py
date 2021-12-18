user = str(input("Entet Something: "))
length_name = len(user) #calculate length of the list
String_name = user[length_name::-1]
if user == "":
    print("Nothing Not Display.")
else:
    print(String_name)
