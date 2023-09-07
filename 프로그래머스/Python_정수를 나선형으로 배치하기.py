def solution(n):
    answer = [[0] * n for _ in range(n)]
    up = False
    down = False
    left = False
    right = True
    count = 1
    i = 0
    j = 0
    while True:
        if count == n**2 + 1:
            break
        if right:
            while j < n and answer[i][j] == 0:
                answer[i][j] = count
                count += 1
                j += 1
            j -= 1
            i += 1
            right = False
            down = True
        elif down:
            while i < n and answer[i][j] == 0:
                answer[i][j] = count
                count += 1
                i += 1
            i -= 1
            j -= 1
            down = False
            left = True
        elif left:
            while j >= 0 and answer[i][j] == 0:
                answer[i][j] = count
                count += 1
                j -= 1
            j += 1
            i -= 1
            left = False
            up = True
        elif up:
            while i >= 0 and answer[i][j] == 0:
                answer[i][j] = count
                count += 1
                i -= 1
            i += 1
            j += 1
            up = False
            right = True
    return answer


# 테스트 케이스
print(solution(4))
print(solution(5))

"""
틀린 내 코드
달팽이 수열 어렵네... 나중에 꼭 다시 풀어보자
다른 사람 풀이는 그때 가서 보자

def solution(n):
    answer = [[0]*n]*n
    up = False
    down = False
    left = False
    right = True
    count = 1
    i = 0
    j = 0
    while True:
        if count == n**2 + 1:
            break
        elif right:
            if j < n:
                if answer[i][j] == 0:
                    answer[i][j] = count
                    count += 1
                    j += 1
                else:
                    j -= 1
                    i += 1
                    right = False
                    down = True
            else:
                right = False
                down = True
                j -= 1
                i += 1
        elif down:
            if i < n:
                if answer[i][j] == 0:
                    answer[i][j] = count
                    count += 1
                    i += 1
                else:
                    i -= 1
                    j -= 1
                    down = False
                    left = True
            else:
                i -= 1
                j -= 1
                down = False
                left = True
        elif left:
            if j >= 0:
                if answer[i][j] == 0:
                    answer[i][j] = count
                    count += 1
                    j -= 1
                else:
                    i -= 1
                    j += 1
                    left = False
                    up = True
            else:
                i -= 1
                j += 1
                left = False
                up = True
        elif up:
            if i >= 0:
                if answer[i][j] == 0:
                    answer[i][j] = count
                    count += 1
                    i -= 1
                else:
                    i += 1
                    j -= 1
                    up = False
                    right = True
            else:
                i += 1
                j -= 1
                up = False
                right = True
    return answer


# 테스트 케이스
print(solution(4))
print(solution(5))



Traceback (most recent call last):
  File "/tmp/main.py", line 2, in <module>
    import user_code
  File "/tmp/user_code.py", line 81, in <module>
    print(solution(4))
          ^^^^^^^^^^^
  File "/tmp/user_code.py", line 31, in solution
    if answer[i][j] == 0:
       ~~~~~~~~~^^^
IndexError: list index out of range

[Execution complete with exit code 1]

"""
