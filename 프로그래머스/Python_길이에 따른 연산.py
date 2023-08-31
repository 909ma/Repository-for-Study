def solution(num_list):
    if len(num_list) // 11:
        answer = sum(num_list)
    else:
        answer = 1
        for item in num_list:
            answer *= item
    return answer


print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))

"""
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))

eval() 함수를 봐놓고 쓰지를 못하네
"""
