A, B, C = map(int, input().split())
D = int(input())

while True:
    if D >= 60:
        B += 1
        D -= 60
    else:
        C += D
        break

while True:
    if C >= 60:
        B += 1
        C -= 60
    else:
        break

while True:
    if B >= 60:
        A += 1
        B -= 60
    else:
        break

while True:
    if A >= 24:
        A -= 24
    else:
        break

print(f"{A} {B} {C}")
