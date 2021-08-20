def checksum(sum,b):
    mem = {}
    for i in range(0,len(b)):
        for j in range(0,len(b)):
            if b[i]+b[j] == sum:
                return True
    return False

tc = int(input())
for i in range(0,tc):
    a = input().strip().split()
    b = list(map(int,input().strip().split()))
    sum = int(a[1])
    print(checksum(sum,b))
