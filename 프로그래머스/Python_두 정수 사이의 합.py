def solution(a, b):
    return sum(i for i in range(min(a, b), max(a, b) + 1))


# Test Cases
print(solution(3, 4))
print(solution(3, 3))
print(solution(5, 3))


"""
def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


# Test Cases
print(solution(3, 4))
print(solution(3, 3))
print(solution(5, 3))


이게 낫네
"""
"""
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))


수학 공부한거 다 버렸네...
"""
