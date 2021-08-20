s = input()
check = "010"
ctr = 0
for i in range(0,len(s)-3):
    k = s[i:i+3]
    if k == check:
        ctr+=1
print(ctr)

