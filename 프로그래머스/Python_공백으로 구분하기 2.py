def solution(my_string):
    answer = my_string.strip().split()
    return answer


print(solution(" i    love  you"))
print(solution("    programmers  "))


"""
solution=lambda x:x.split()

strip() 없어도 되네
"""
