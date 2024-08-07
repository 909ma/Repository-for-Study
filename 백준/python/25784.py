num1, num2, num3 = map(int, input().split(' '))

if num1 + num2 == num3:
    print(1)
elif num2 + num3 == num1:
    print(1)
elif num1 + num3 == num2:
    print(1)
elif num1*num2 == num3:
    print(2)
elif num2*num3 == num1:
    print(2)
elif num1*num3 == num2:
    print(2)
else:
    print(3)

"""
a,b,c=sorted(map(int,input().split()))
print((a+b!=c)*2+(a*b!=c))


ㅇㅎ
"""

