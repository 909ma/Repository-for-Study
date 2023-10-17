"""
이거 안 됨

def solution(people, limit):
    answer = 0
    people.sort()
    for i, item in enumerate(people):
        if item == -1:
            pass
        elif limit - item < 40:
            answer += 1
        else:
            max_weight = limit - item
            for j in range(i + 1, len(people)):
                if people[j] <= max_weight:
                    people[j] = -1
                    break
            answer += 1
    return answer


# Test Cases
print(solution([70, 50, 80, 50], 100) == 3)
print(solution([70, 80, 50], 100) == 3)
"""
