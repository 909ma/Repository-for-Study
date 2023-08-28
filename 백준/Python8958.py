testCase = int(input())
for _ in range(testCase):
    OX = input()
    length = len(OX)
    score = 0
    combo = 0
    check = False
    for j in range(length):
        if OX[j] == 'O' and not check:
            check = True
            combo += 1
            score += combo
        elif OX[j] == 'O' and check:
            combo += 1
            score += combo
        elif OX[j] == 'X':
            combo = 0
            check = False
    print(score)
