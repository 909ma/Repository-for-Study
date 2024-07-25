def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
search_cards = list(map(int, input().split()))

cards.sort()  # 이분 탐색을 위해 정렬

result = []

for num in search_cards:
    result.append(binary_search(cards, num))

print(" ".join(str(int(found)) for found in result))
