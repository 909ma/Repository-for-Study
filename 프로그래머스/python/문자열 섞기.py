def solution(str1, str2):
    answer = ""
    size = len(str1)
    for i in range(size):
        answer += str1[i] + str2[i]
    return answer
