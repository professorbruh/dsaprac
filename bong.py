def answeru(arr,i,j,memo={}):
    tmp = str(i)+','+str(j)
    if(i==0 or j ==0):
        memo[tmp] = arr[i][j]
        return memo[tmp]
    if tmp in memo:
        return memo[tmp]
    else:
        memo[tmp] = min(answeru(arr,i-1,j,memo) , answeru(arr,i,j-1,memo)) + arr[i][j]
    return memo[tmp]

cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(answeru(cost, 2, 2))