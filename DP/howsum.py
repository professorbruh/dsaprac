def howsum(tsum,n,mem = {}):
    if tsum == 0:
        return []
    if tsum < 0:
        return None
    if tsum in mem:
        return mem[tsum]
    for i in n:
        rem = tsum - i
        remres = howsum(rem,n,mem)
        if remres is not None:
            k = remres + [i]
            mem[tsum] = k
            return mem[tsum]
    mem[tsum] = None
    return None

print(howsum(7,[2,3]))

