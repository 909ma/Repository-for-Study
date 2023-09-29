def solution(s):
    command = list(s.split())
    answer = 0
    temp = 0
    for item in command:
        if item == 'Z':
            answer -= temp
        else:
            temp = int(item)
            answer += temp
    return answer


# Test Cases
print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))


"""
def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)
    
    
잘 풀었네
"""
