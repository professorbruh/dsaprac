def con(t,s):
    if t == '':
        return [[]]
    res = []
    for i in s:
        if t.startswith(i):
            suffix = t[len(i):]
            s_ways = con(suffix, s)
            t_ways = []
            for j in range(0,len(s_ways)):
                t_ways = t_ways + ([i] + s_ways[j])
            res.append(t_ways)

    return res



print(*con('purple',['purp','p','ur','le','purp']))

