def solution(s):
    if len(s) == 4 or len(s) == 6:
        s = s.replace('1', '')
        s = s.replace('2', '')
        s = s.replace('3', '')
        s = s.replace('4', '')
        s = s.replace('5', '')
        s = s.replace('6', '')
        s = s.replace('7', '')
        s = s.replace('8', '')
        s = s.replace('9', '')
        s = s.replace('0', '')
        if len(s) != 0:
            return False
        else:
            return True
    else:
        return False


# Test Cases
print(solution("a234"))
print(solution("1234"))



"""
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def alpha_string46(s):
    #함수를 완성하세요

    return s.isdigit() and len(s) in [4,6]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )



isdigit()가 생각이 안 나더라
"""