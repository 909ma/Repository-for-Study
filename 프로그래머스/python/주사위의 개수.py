def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)


# Test Cases
print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))
