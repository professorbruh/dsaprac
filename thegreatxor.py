x = int(input())
ctr = 0
for a in range(1,x):
    k = a ^ x
    if k > x:
        ctr+=1

print(ctr)