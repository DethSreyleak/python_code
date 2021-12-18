a = int(input())
res = {}
for i in range(a):
    s, t = input().split()
    res.update({int(t):s})
b = list(res.keys())
b.sort()
print(res.get(b[-2]))