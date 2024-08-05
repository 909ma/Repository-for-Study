n = int(input())
roll = list(map(int, input().split(' ')))
is_search = False
for i in range(6, 0, -1):
    if roll.count(i) == 1:
        print(roll.index(i) + 1)
        is_search = True
        break
if not is_search:
    print("none")

"""
s=[*open(0)][1].split()
print([*max(1//s.count(i)*[i,s.index(i)+1]for i in s),0,'none'][1])


???
"""
