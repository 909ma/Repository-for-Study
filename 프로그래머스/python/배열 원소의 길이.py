def solution(strlist):
    answer = []
    for item in strlist:
        answer.append(len(item))
    return answer


# Test Cases
print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))


"""
def solution(strlist):
    answer = list(map(len, strlist))
    return answer
    
    
이렇게 풀면 되네
"""
