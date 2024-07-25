testCase = int(input())
for _ in range(testCase):
    a, b = map(int, input().split())
    list1 = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
    a %= 10
    b %= len(list1[a])
    num = list1[a][b-1]
    if num == 0:
        print(10)
    else:
        print(num)
"""
0   0
1   1
2   2 4 8 6
3   3 9 7 1
4   4 6
5   5
6   6
7   7 9 3 1
8   8 4 2 6
9   9 1
"""
