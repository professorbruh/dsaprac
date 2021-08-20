def canusum(tsum, n, memo={}):
    if tsum in memo:
        return memo[tsum]
    if tsum == 0:
        return True
    if tsum < 1:
        return False
    for i in n:
        rem = tsum - i
        if canusum(rem, n, memo):
            return True
    memo[tsum] = False
    return False


print(canusum(7,[5,3,4,1]))
print(canusum(300,[7,14]))
