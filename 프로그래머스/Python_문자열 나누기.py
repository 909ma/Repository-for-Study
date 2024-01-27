def solution(s):
    answer = 0
    
    count1 = 0
    count2 = 0
    char1 = ''
    
    for item in s:
        if char1 == '':
            char1 = item
            count1 = 1
        else:
            if char1 == item:
                count1 += 1
            else:
                count2 += 1
            
            if count1 == count2:
                answer += 1
                count1 = 0
                count2 = 0
                char1 = ''
                
    if char1 != '':
        answer += 1
        
    return answer


"""
https://school.programmers.co.kr/learn/courses/30/lessons/140108
"""
