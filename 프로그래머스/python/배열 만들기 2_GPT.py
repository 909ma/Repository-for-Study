def solution(l, r):
    answer = []

    for num in range(l, r + 1):
        if all(digit in '05' for digit in str(num)):
            answer.append(num)

    if not answer:
        return [-1]

    return answer

print(solution(5, 555))
print(solution(10, 20))


"""
`if all(digit in '05' for digit in str(num)):` 이 부분은 주어진 숫자 `num`이 숫자 "0"과 "5"로만 이루어져 있는지를 확인하는 조건문입니다. 이 부분은 파이썬의 리스트 컴프리헨션과 `all()` 함수를 사용한 표현입니다.

여기서 간단한 설명을 제공하겠습니다:

1. `str(num)`: 정수 `num`을 문자열로 변환합니다. 이렇게 하면 숫자를 문자열로 변환한 후 문자열의 각 문자(숫자)에 접근할 수 있습니다.

2. `for digit in str(num)`: 문자열 `str(num)` 안에 있는 각 문자(숫자)를 하나씩 순회합니다. `digit` 변수에는 현재 순회 중인 문자(숫자)가 들어갑니다.

3. `digit in '05'`: 현재 순회 중인 문자(숫자) `digit`이 문자열 `'05'` 안에 존재하는지를 확인합니다. 즉, `digit`이 "0" 또는 "5"인 경우에는 `True`를 반환하고, 그렇지 않으면 `False`를 반환합니다.

4. `all(...)`: `all()` 함수는 인자로 받은 조건들이 모두 `True`일 때 `True`를 반환합니다. 여기서는 주어진 숫자 `num`의 모든 자릿수가 "0" 또는 "5"로만 이루어져 있으면 조건이 참이 됩니다.

따라서 이 조건문은 주어진 숫자 `num`이 숫자 "0"과 "5"로만 이루어져 있는 경우에만 참이 되며, 그렇지 않은 경우에는 거짓이 됩니다.
"""
"""
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]


머리 잘 썼네...
"""
