def solution(s):
    answer = []
    char_list = []
    for i in range(len(s)):
        if s[i] in char_list:
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    answer.append(i-j)
                    break
        else:
            answer.append(-1)
            char_list.append(s[i])
    return answer


# Test Cases
print(solution("banana"))
print(solution("foobar"))
