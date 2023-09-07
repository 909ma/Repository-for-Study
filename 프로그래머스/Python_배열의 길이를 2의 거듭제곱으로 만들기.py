def solution(arr):
    while True:
        if check(len(arr)):
            return arr
        else:
            arr.append(0)
    return arr


def check(num):
    while True:
        if num == 1:
            return True
        elif num % 2:
            return False
        else:
            num //= 2


print(solution([1, 2, 3, 4, 5, 6]))
print(solution([58, 172, 746, 89]))


"""
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)

2의 거듭제곱 확인 방법 O(1)로 해야 겨우 O(n)
logn으로 확인하면 그걸 n번 반복 -> o(nlogn)
길이 1000개 -> 가장 빠른방법은 각각 하드코딩하기 겨우 10개


라고 하네요~
"""
