s = input()
n = int(input())
ctr = 0
for i in range(0,len(s)):
    if s[i] == 'a':
        ctr+=1
q = n//len(s)
rem = n%len(s)
ctr = ctr*q
for i in range(0,rem):
    if s[i]=='a':
        ctr+=1

print(ctr)
