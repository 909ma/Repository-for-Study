def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += f"{i}" * (food[i] // 2)
    return answer + "0" + answer[::-1]


# Test Cases
print(solution([1, 3, 4, 6]) == "1223330333221")
print(solution([1, 7, 1, 2]) == "111303111")


"""
def solution(food):
    answer = ''
    for i,n in enumerate(food[1:]):
        answer += str(i+1) * (n//2)
    return answer + "0" + answer[::-1]
    
    
enumerate() 잘 써보자
"""
"""
def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer
    
    
진짜로 앞뒤로 붙였네"""
