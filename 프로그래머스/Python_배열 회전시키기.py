def solution(numbers, direction):
    if direction == "left":
        answer = numbers[1:]
        answer.append(numbers[0])
    else:
        answer = numbers[-1:]
        answer += numbers[:-1]
    return answer


# Test Cases
print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
