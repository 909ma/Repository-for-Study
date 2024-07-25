def solution(s):
    answer = []
    for item in s:
        if item == '(':
            answer.append('(')
        else:
            if len(answer) == 0:
                return False
            elif answer.pop() == '(':
                pass
            else:
                return False
    return True if len(answer) == 0 else False


# Test Cases
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))


"""
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# def is_pair(s):
#     x = [without for without in s if without == '(' or without == ')']
#     ind_x = [ i for i,n in enumerate(x) if n == '(' ]
#     ind_y = [ i for i,n in enumerate(x) if n == ')' ]
#     if len(ind_x) == len(ind_y):
#         for value in ind_x:
#             if value%2 != 0:
#                 return False     
#         return True

#     else: 
#         return False
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair("()()()"))


와 잘한다
"""

"""
def solution(s):
    answer = []
    for item in s:
        if item == '(':
            answer.append('(')
        else:
            try:
                answer.pop()
            except:
                return False
    return len(answer) == 0
    

개선시킨 내 풀이
"""
