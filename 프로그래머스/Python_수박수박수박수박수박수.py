def solution(n):
    return ''.join(["박" if i % 2 else "수" for i in range(n)])


# Test Cases
print(solution(3))
print(solution(4))


"""
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def water_melon(n):
    # 함수를 완성하세요.

    return "수박" * (n//2) + "수" * (n%2)


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));


이렇게 할 껄 그랬나
"""
