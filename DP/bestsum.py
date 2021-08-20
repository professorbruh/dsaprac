def bestsum(sum,n,mem = {}):
    if sum == 0:
        return []
    if sum < 0 :
        return None
    if sum in mem:
        return mem[sum]
    sc = None

    for i in n:
        rem = sum - i
        rem_comb = bestsum(rem, n)
        if rem_comb is not None:
            comb = rem_comb + [i]
            if sc is None or len(comb) < len(sc):
                sc = comb

    mem[sum] = sc
    return mem[sum]


print(bestsum(300,[3,4,5,6]))