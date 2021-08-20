def gridtrav(m,n):
    mat = [[0]*(n+1) for _ in range(m+1)]
    mat[1][1] = 1

    for i in range(0,m+1):
        for j in range(0,n+1):
            cur = mat[i][j]
            if j+1<=n:
                mat[i][j+1] = mat[i][j+1] + cur

            if i+1<=m:
                mat[i+1][j] = mat[i+1][j] + cur
    return mat[m][n]

print(gridtrav(18,18))



