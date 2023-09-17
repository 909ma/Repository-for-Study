def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_last(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            if mid == len(arr) - 1 or arr[mid + 1] != target:
                return mid
            else:
                left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    first_idx = binary_search_first(cards, target)
    last_idx = binary_search_last(cards, target)

    if first_idx == -1:
        print(0, end=' ')
    else:
        print(last_idx - first_idx + 1, end=' ')
