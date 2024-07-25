def solution(strings, n):
    answer = []
    for item in strings:
        temp_str = item[n] + item[0:n] + item[n+1:]
        answer.append(temp_str)
    answer.sort()
    return [item[1:1+n] + item[0] + item[1+n:] for item in answer]


# Test Cases
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))


"""
def solution(strings, n):
    new =[]
    answer =[]
    for i in range(len(strings)):
        a = strings[i][n]
        b = a+strings[i]
        new.append(b)
    new.sort()
    for i in range(len(new)):
        c = new[i][1:]
        answer.append(c)
    return answer
    
    
??? 이런 방법이??
"""
