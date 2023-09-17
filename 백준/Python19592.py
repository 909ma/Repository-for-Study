test_case = int(input())
for _ in range(test_case):
    N, X, Y = map(int, input().split())
    inputs_origin = list(map(int, input().split()))
    inputs_sort = sorted(inputs_origin, reverse=True)
    my_velocity = inputs_origin[N-1]
    if my_velocity == inputs_sort[0]:
        if my_velocity > inputs_sort[1]:
            print(0)

        else:
            if Y != 0:
                print(1)
            else:
                print(-1)
    else:
        if X % inputs_sort[0] == 0:
            min_time = X // inputs_sort[0]
        else:
            min_time = X / inputs_sort[0]

        temp = (min_time - 1) * my_velocity + Y
        if temp <= X:
            print(-1)
        else:
            print(int((X - (min_time - 1) * my_velocity + 1)//1))
