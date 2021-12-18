N = list(map(int, input().split()))
arr = sorted(N)
A =  arr[2] - arr[1]
B = arr[1] - arr[0]
if A==B:
    print("Yes")
else:
    print("No")