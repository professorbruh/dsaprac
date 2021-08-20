s = input()
dp = [[False for i in range(len(s))] for j in range(len(s))]

for i in range(len(s)):
    dp[i][i] = True
    if i < len(s) - 2 and s[i] == s[i + 1]:
        dp[i][i + 1] = True

low = float("inf")
up = -1
for i in range(len(s)):
    for j in range(len(s)):
        try:
            if s[i] == s[j] and dp[i+1][j-1]:
                print("here",i," ",j)
                dp[i][j] = True
        except:
            continue
for i in range(len(s)):
    print(dp[i])