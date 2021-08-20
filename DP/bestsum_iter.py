def bestsum(n,arr):
    dp = [None for i in range(n+1)]
    dp[0] = []
    for i in range(n+1):
        if dp[i] != None:
            for j in arr:
                if i+j <= n :
                    temp = [f for f in dp[i]]
                    temp.append(j)
                    if len(temp) < len(dp[i]) or dp[i+j] == None:
                        dp[i+j] = temp
    return dp[n]

sum = int(input().strip())
arr = list(map(int,input().strip().split()))
print(bestsum(sum,arr))

#