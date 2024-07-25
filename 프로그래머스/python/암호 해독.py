def solution(cipher, code):
    answer = ''
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
    return answer


# Test Cases
print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))


"""
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

    
    
이걸 까먹었네
"""
