import random
user = int(input("Enter a number: "))
for i in range(user):
    answer = random.randint(0, user)
    print(answer)