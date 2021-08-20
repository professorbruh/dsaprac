def cons(t, s, mem={}):
    if t == '':
        return 1
    if t in mem:
        return mem[t]
    count = 0
    for i in s:
        if t.startswith(i):
            suffix = t[len(i):len(t)]
            nums = cons(suffix,s)
            count += nums
    mem[t] = count
    return count


print(cons('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eeee','eeeeeeee','eeeeeeeeeeee']))