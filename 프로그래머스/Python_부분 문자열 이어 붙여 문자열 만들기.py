def solution(my_strings, parts):
    answer = ""
    for i in range(len(parts)):
        answer += my_strings[i][parts[i][0] : parts[i][1] + 1]
    return answer


print(
    solution(
        ["progressive", "hamburger", "hammer", "ahocorasick"],
        [[0, 4], [1, 2], [3, 5], [7, 7]],
    )
)


"""
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer
    

enumerate()를 알아야겠네
"""
