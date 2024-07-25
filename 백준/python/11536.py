import copy


size = int(input())
inputs = []
for i in range(size):
    inputs.append(input())

upList = copy.deepcopy(inputs)
upList.sort(reverse=False)
downList = copy.deepcopy(inputs)
downList.sort(reverse=True)

if inputs == upList:
    print("INCREASING")
elif inputs == downList:
    print("DECREASING")
else:
    print("NEITHER")

"""
n,*s=open(0)
t=sorted(s)
print(["NEITHER","INCREASING","DECREASING"][(s==t)-(s==t[::-1])])

진짜 잘하네;;;
"""
