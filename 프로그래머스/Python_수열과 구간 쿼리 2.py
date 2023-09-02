def solution(numLog):
    answer = ''
    for i in range(len(numLog)):
        if i == 0:
            temp = numLog[0]
        else:
            gap = numLog[i] - temp
            if gap == 1:
                answer += "w"
            elif gap == -1:
                answer += "s"
            elif gap == 10:
                answer += "d"
            else:
                answer += "a"
            temp = numLog[i]
    return answer


print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))

"""
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res


토요일이라 대충 풀었나, 나보다 좋은 풀이가 수두룩하네
"""
