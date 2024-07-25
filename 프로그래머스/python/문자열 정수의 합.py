def solution(num_str):
    answer = 0
    for i in range(len(num_str)):
        answer += int(num_str[i])
    return answer


print(solution("123456789"))
print(solution("1000000"))

"""
def solution(num_str):
    return sum(map(int, num_str))
    
map이 이렇게도 되네
"""
