N, A, B = map(int, input().split())
if A > B and B >= N:
    print('Subway')
elif A == B and B >= N:
    print('Anything')
else:
    print('Bus')
