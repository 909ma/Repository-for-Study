def solution(my_string):
    answer = []
    for _ in range(52):
        answer.append(0)

    for i in range(len(my_string)):
        temp_char = my_string[i]
        temp_int = ord(temp_char)
        if temp_char >= 'a' and temp_char <= 'z':
            temp = temp_int - ord('a') + 26
            answer[temp] += 1
        else:
            temp = temp_int - ord('A')
            answer[temp] += 1
    return answer


print(solution("Programmers"))


"""
def solution(my_string):
    answer=[0]*52
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65]+=1
        else:
            answer[ord(x)-71]+=1
    return answer
    
    
잘했네...
"""
"""
def solution(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']

    
이런 풀이가 ㅋㅋ
"""
