def solution(my_string, target):
    answer = int(target in my_string)
    return answer

print(solution("banana", "ana"))
print(solution("banana", "wxyz"))
