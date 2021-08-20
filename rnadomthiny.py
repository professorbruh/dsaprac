import random
import csv
c1 = ord('A')
c2 = ord('Z')
n1 = ord('0')
n2 = ord('9')
s = ""
k=csv.writer()
while 1:
    for i in range(0, 12):
        k = random.randint(0, 1)
        if k == 1:
            s += chr(random.randint(c1, c2))
        else:
            s += chr(random.randint(n1, n2))

    print(s)


