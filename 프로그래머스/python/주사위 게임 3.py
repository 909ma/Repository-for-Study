def solution(a, b, c, d):
    answer = 0
    num_list = [a, b, c, d]
    num_set = list(set(num_list))
    size = len(num_set)
    if size == 1:
        answer = 1111 * a
    elif size == 2:
        for target in num_set:
            count = 0
            for item in num_list:
                if target == item:
                    count += 1
            if count == 3:
                if target == num_set[0]:
                    answer = (10 * num_set[0] + num_set[1]) ** 2
                    break
                else:
                    answer = (10 * num_set[1] + num_set[0]) ** 2
                    break
            elif count == 2:
                answer = (num_set[0] + num_set[1]) * abs(num_set[0] - num_set[1])
                break
    elif size == 3:
        for target in num_set:
            count = 0
            for item in num_list:
                if target == item:
                    count += 1
            if count == 2:
                answer = num_set[0] * num_set[1] * num_set[2] / target
                break
    else:
        answer = min(num_set)
    return answer


print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
print(solution(6, 3, 3, 6))
print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))


"""
평소에는 1 ~ 2점 주더니 이건 8점 주네
"""
"""
def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        answer=1111*a
    elif a==b==c:
        answer=(10*a+d)**2
    elif a==b==d:
        answer=(10*a+c)**2
    elif a==c==d: 
        answer=(10*a+b)**2
    elif b==c==d:
        answer=(10*d+a)**2
    elif a==b and c==d:
        answer=(a+c)*abs(a-c)
    elif a==c and b==d:
        answer=(a+b)*abs(a-b)
    elif a==d and b==c:
        answer=(a+b)*abs(a-b)
    elif a==b:
        answer=c*d
    elif a==c:
        answer=b*d
    elif a==d:
        answer=b*c
    elif b==c:
        answer=a*d
    elif b==d:
        answer=a*c
    elif c==d:
        answer=a*b
    else:
        answer=min(a,b,c,d)

    return answer
    
    
나보다 낫다;;
"""
"""def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)
        
        
count() 뭔데...
index() 같은 것도 있네
"""
