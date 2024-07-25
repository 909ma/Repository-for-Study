def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[i] * n
    return answer


# Test Cases
print(solution("hello", 3))


"""
def solution(my_string, n):
    return ''.join(i*n for i in my_string)
    

    
join 잘 쓰네
"""
