def solution(num_list):
    answer = 1
    for item in num_list:
        answer *= item
    temp = sum(num_list)**2

    if temp > answer:
        answer = 1
    else:
        answer = 0    
    return answer


print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))


'''
def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0
    
eval() 쓰는 생각을 해보자
'''
