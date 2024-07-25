def solution(my_string, queries):
    answer = ''
    for item in queries:
        a, b = item
        temp = my_string[a:b + 1]
        my_string = my_string[:a] + temp[::-1] + my_string[b+1:]
        # print(my_string[:a])
        # print(temp[::-1])
        # print(my_string[b+1:])
        # print()
        # print("="*50)
    return my_string


print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]	))


"""
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)


깔끔하네
"""
