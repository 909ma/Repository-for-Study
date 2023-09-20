X, Y = map(int, input().split())
current_win_rate = (Y * 100) // X

if current_win_rate >= 99:
    print(-1)
else:
    low, high = 0, 1000000000
    answer = -1
    while low <= high:
        mid = (low + high) // 2
        new_win_rate = ((Y + mid) * 100) // (X + mid)
        if new_win_rate > current_win_rate:
            high = mid - 1
            answer = mid
        else:
            low = mid + 1
    print(answer)
