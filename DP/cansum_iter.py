def cansum(sum,arr):
    dp = [False]*(sum+1)
    dp[0] = True
    for i in range(0,sum+1):
        if dp[i]:
            for j in arr:
                if i + j <= sum:
                    dp[i + j] = True
    print(dp)

a = int(input())
b = list(map(int,input().strip().split()))
cansum(a,b)