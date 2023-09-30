def solution(numlist, n):
    answer = []
    temp_list = []
    for item in numlist:
        temp_list.append(abs(item - n))
    temp_list.sort()

    for item in temp_list:
        if n + item in numlist:
            answer.append(n + item)
            del numlist[numlist.index(n + item)]
        else:
            answer.append(n - item)
            del numlist[numlist.index(n - item)]
    return answer


# Test Cases
print(solution([1, 2, 3, 4, 5, 6], 4))
print("="*50)
print(solution([10000, 20, 36, 47, 40, 6, 10, 7000], 30))
print("="*50)


"""
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer
    
    
이렇게 할까 했었는데 괜찮았네
"""
