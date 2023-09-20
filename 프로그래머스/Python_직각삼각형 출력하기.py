n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()


"""
n = int(input())
for i in range(1,n+1):
    print('*'*i)
    
    
아 여긴 파이썬이지
"""
"""
print('\n'.join('*' * (i + 1) for i in range(int(input()))))


깔끔하네
"""
