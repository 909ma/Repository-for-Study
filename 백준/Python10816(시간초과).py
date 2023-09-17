def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            while arr[mid] == target:
                mid -= 1
                if mid == -1:
                    break
            mid += 1
            while arr[mid] == target:
                count += 1
                mid += 1
                if mid == len(arr):
                    break
            return count
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return count


card_num = int(input())
inputs = sorted(map(int, input().split()))

cases = int(input())
target = list(map(int, input().split()))
for i in range(cases):
    temp = binary_search(inputs, target[i])
    print(f"{temp} ")
