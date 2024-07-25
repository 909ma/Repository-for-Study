def solution(dartResult):
    answer = 0
    temp = ''
    score_list = []
    i = 0
    for item in dartResult:
        if item.isdigit():
            temp += item
        else:
            if item == 'S':
                score_list.append(int(temp) ** 1)
                i += 1
            elif item == 'D':
                score_list.append(int(temp) ** 2)
                i += 1
            elif item == 'T':
                score_list.append(int(temp) ** 3)
                i += 1
            elif item == '*':
                score_list[i - 1] = score_list[i - 1] * 2
                if i - 2 >= 0:
                    score_list[i - 2] = score_list[i - 2] * 2
            elif item == '#':
                score_list[i - 1] = score_list[i - 1] * (-1)
            temp = ''
    answer = sum(score_list)
    return answer


"""
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


이게 머임ㅋㅋㅋ
"""
