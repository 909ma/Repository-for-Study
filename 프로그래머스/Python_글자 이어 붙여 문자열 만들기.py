def solution(my_string, index_list):
    answer = ''
    for item in index_list:
        answer += my_string[item]
    return answer


print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
print(solution("zpiaz", [1, 2, 0, 0, 3]))


"""
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])

잘했네...
"""
"""
def solution(my_string, index_list):
    return ''.join(map(lambda x: my_string[x], index_list))

이렇게도 했네
"""
