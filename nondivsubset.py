nums1 = input()
nums1.strip()
arr = list(map(int,nums1.split(' ')))
k = int(input("Enter k"))
l = [0]*k
for i in range(0,len(arr)):
    l[arr[i] % k] += 1
fin = min(l[0],1)
for i in range(1,(k//2)+1):
    if i != k-i:
        fin += max(l[i],l[k-i])
    else:
        fin += min(l[i],1)
print(fin)


