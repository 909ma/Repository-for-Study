def solution(n, arr1, arr2):
    answer = []
    for map1, map2 in zip(arr1, arr2):
        temp = f"{map1 | map2:016b}"
        print(temp[-n:])
        answer.append(temp[-n:].replace("1", "#").replace("0", " "))
    return answer


# Test Cases
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))


"""
def solution(n, *maps):
    return [line(n, a | b) for a, b in zip(*maps)]


def line(n, x):
    return ''.join(' #'[int(i)] for i in f'{x:016b}'[-n:])


def test_sample():
    assert solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) == [
        '#####',
        '# # #',
        '### #',
        '#  ##',
        '#####',
    ]
    assert solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]) == [
        '######',
        '###  #',
        '##  ##',
        ' #### ',
        ' #####',
        '### # ',
    ]


def test_line():
    assert line(5, 9) == ' #  #'
    assert line(5, 30) == '#### '
    assert line(5, 9 | 30) == '#####'
    
    
    
더 나은 풀이를 만들 수 있었네
' '이랑 '#' 두 개니까 0과 1을 사용해서 변환하기 생각하자
"""
