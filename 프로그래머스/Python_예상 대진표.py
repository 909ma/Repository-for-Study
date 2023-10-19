def solution(n, a, b):
    a = f"{a - 1:020b}"
    b = f"{b - 1:020b}"
    answer = 20
    for i, j in zip(a, b):
        if i == j:
            answer -= 1
        else:
            break
    return answer


# Test Cases
print(solution(8, 4, 7) == 3)
print(solution(8, 4, 8) == 3)

"""
1 0001 > 0000
2 0010 > 0001

3 0011 > 0010
4 0100 > 0011

5 0101 > 0100
6 0110 > 0101

7 0111 > 0110
8 1000 > 0111
"""


"""
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
    
    
.bit_length() 머임;"""
