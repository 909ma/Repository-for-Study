def solution(picture, k):
    answer = []
    for item in picture:
        temp = ""
        for i in range(len(item)):
            for _ in range(k):
                temp += item[i]
        for _ in range(k):
            answer.append(temp)
    return answer


# 테스트 케이스
print(solution([".xx...xx.", "x..x.x..x", "x...x...x",
      ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2))
print(solution(["x.x", ".x.", "x.x"], 3))

"""
x.x
.x.
x.x
"""

"""
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer
    
    
이렇게도 할 수 있구나
"""
