def cons(t,s,mem = {}):
    if t == '':
        return True
    if t in mem:
        return mem[t]

    for i in s:
        if i in s:
            if t.startswith(i):
                suffix = t[len(i):len(t)]
                if cons(suffix, s):
                    mem[t] = True
                    return mem[t]
    mem[t] = False
    return False


print(cons('abcdef',['ab','abc','cd','def','abcd']))





