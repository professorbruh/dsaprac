def gridtraveller(m, n, mem = {}):
    key = str(m) +','+str(n)
    print(mem)
    if key in mem:
        return mem[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    mem[key] = gridtraveller(m-1,n,mem)+gridtraveller(m,n-1,mem)
    return mem[key]

print(gridtraveller(18,18))