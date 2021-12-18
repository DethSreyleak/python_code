user = input("Enter something: ")
list_string = []
count = 1
for i in user.upper():
 list_string.append(i + i.lower()*(count-1))
 count += 1
print('-'.join(list_string))