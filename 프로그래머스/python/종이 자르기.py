def solution(M, N):
    return min(M, N) - 1 + min(M, N) * (max(M, N) - 1)


# Test Cases
print(solution(2, 2))
print("="*50)
print(solution(2, 5))
print("="*50)
print(solution(1, 1))


"""
def solution(M, N):
    return (M * N) - 1
    
    
아
"""
