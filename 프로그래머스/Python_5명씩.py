def solution(names):
    answer = names[::5]
    return answer


print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))


"""
def solution(names):
    answer1 = names[:1]
    answer2 = names[5:6]
    answer3 = names[10:11]
    answer4 = names[15:16]
    answer5 = names[20:21]
    answer6 = names[25:26]
    answer7 = names[30:31]
    answer = answer1 +answer2+answer3+answer4+answer5+answer6+answer7
    return answer


프로그래머스가 진건가, 이 사람이 이긴건가
"""
