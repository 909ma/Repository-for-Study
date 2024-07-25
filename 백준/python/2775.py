testCase = int(input())

for _ in range(testCase):
    k = int(input())
    n = int(input())
    apartment = [[0] * n for _ in range(k + 1)]

    for i in range(n):
        apartment[0][i] = i + 1

    for i in range(1, k + 1):
        for j in range(n):
            apartment[i][j] = sum(apartment[i - 1][:j + 1])

    print(apartment[k][n - 1])
