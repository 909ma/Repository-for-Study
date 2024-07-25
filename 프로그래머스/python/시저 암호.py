def solution(s, n):
    small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    large = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    answer = ''
    for item in s:
        if item in small:
            answer += small[(small.index(item) + n) % 26]
        elif item in large:
            answer += large[(large.index(item) + n) % 26]
        else:
            answer += item
    return answer


# Test Cases
print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))


"""
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))



chr()이 생각이 안 났어
"""
"""
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def caesar(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i is " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])
    return "".join(result)


list 왜 썼냐 진짜 ㅋㅋ;...
"""
