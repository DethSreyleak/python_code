l = []
a = 1
while a > 0:
    user = str(input())
    l.append(user)
    b = len(l)-1
    if user == "GENERATE":
        for i in range(0, b):
            print("<p>" + l[i] + "</p>")
        a = a-1