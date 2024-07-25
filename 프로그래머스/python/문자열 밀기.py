def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A == B:
            return answer
        else:
            temp = A[-1] + A[:-1]
            A = temp
            answer += 1
    return -1


# Test Cases
print(solution("hello", "ohell"))
print("="*50)
print(solution("apple", "elppa"))
print("="*50)
print(solution("atat", "tata"))
print("="*50)
print(solution("abc", "abc"))
print("="*50)


"""
solution=lambda a,b:(b*2).find(a)


헐ㅋ
"""
