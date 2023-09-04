def solution(x1, x2, x3, x4):
    answer = (x1 | x2) & (x3 | x4)
    return answer


print(solution(False, True, True, True))
print(solution(True, False, False, False))


"""
내가 비트연산자가 약하네
https://dojang.io/mod/page/view.php?id=2460
"""
