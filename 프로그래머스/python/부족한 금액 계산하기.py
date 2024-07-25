def solution(price, money, count):
    answer = (price * (count + 1)) * count / 2 - money
    return  answer if answer >= 0 else 0


# Test Cases
print(solution(3, 20, 4))
print(solution(3, 20, 1))


"""
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
    
    
아오 max()를 생각못했네 진짜
"""