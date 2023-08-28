for _ in range(3):
    num = list(map(int, input().split()))
    count = num.count(0)
    if count == 0:
        print('E')
    elif count == 1:
        print('A')
    elif count == 2:
        print('B')
    elif count == 3:
        print('C')
    elif count == 4:
        print('D')
