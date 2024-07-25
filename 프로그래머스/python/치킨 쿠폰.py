def solution(chicken):
    answer = chicken // 10
    inventory = [chicken % 10, chicken // 10]
    while sum(inventory) >= 10:
        if inventory[0] >= 10:
            inventory[0] -= 10
            inventory[1] += 1
            answer += 1
        elif inventory[1] >= 10:
            inventory[1] -= 10
            inventory[0] += 1
            answer += 1
        elif sum(inventory) >= 10:
            inventory = [0, 1]
            answer += 1
    return answer


# Test Cases
print(solution(100))
print("="*50)
print(solution(1081))
print("="*50)
