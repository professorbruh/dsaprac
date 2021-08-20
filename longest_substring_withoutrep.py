arr = input()
l = arr
i = 0
j = 0
maximum = 0
hash_set = set()
k = list()
while j<len(arr):
    if l[j] not in hash_set:
        hash_set.add(l[j])
        j = j + 1
        if len(hash_set)>maximum:
            maximum = len(hash_set)
    else:
        hash_set.remove(l[i])
        i = i+1

print(maximum)



