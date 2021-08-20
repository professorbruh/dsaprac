import math
a = list(map(int,input().strip().split()))
while a[0] != a[1]:
    if a[0] > a[1]:

        a[0] = a[0] - a[1]
    elif a[1] > a[0]:
        a[1] = a[1] - a[0]
print(a[0])
print(math.gcd(a[0],a[1]))
