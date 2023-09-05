def solution(arr):
    answer = True
    scale = len(arr[0])
    for i in range(scale):
        for j in range(scale):
            if arr[i][j] == arr[j][i]:
                pass
            else:
                answer = False
                return int(answer)
    return int(answer)


"""
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))


와 수학적 감각이 정말 뛰어나네
"""
