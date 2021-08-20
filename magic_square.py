
def xorcheck(n):
    fin = 0
    for i in range(0,len(n)):
        frequency = (i + 1) * (len(n) - i)
        if frequency % 2 == 1:
            fin = fin ^ n[i]
    return fin
print(xorcheck([98,74,12]))
