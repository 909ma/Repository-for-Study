def padovan(n):
    if n <= 2:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    return dp[n]


import sys

testCase = int(sys.stdin.readline().rstrip())
for _ in range(testCase):
    num = int(sys.stdin.readline().rstrip()) - 1
    print(padovan(num))
