def solution(my_string, alp):
    answer = my_string.replace(alp, alp.upper())
    return answer


print(solution("programmers", "p"))
print(solution("lowercase", "x"))
