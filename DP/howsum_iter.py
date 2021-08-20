def howsum(sum,arr):
    dp = [ None for i in range(0,sum+1) ]
    dp[0] = []
    for i in range(sum+1):
        if dp[i] != None:
            for j in arr:
                if i+j <= sum :
                    print(i,"",j)
                    temp = [f for f in dp[i]]
                    temp.append(j)
                    dp[i+j] = temp
    return dp[sum]


sum = int(input().strip())
arr = list(map(int,input().strip().split()))
print(howsum(sum,arr))
