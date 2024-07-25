import math

def min_four_squares(n):
    squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for square in squares:
            if square > i:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)

    return dp[n]

n = int(input())

print(min_four_squares(n))
