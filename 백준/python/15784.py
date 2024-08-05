N, i, j = map(int, input().split(' '))
i -= 1
j -= 1
people_list = []

for k in range(N):
    input_list = list(map(int, input().split(' ')))
    people_list.append(input_list)

max_num = 0

for k in range(N):
    max_num = max(max_num, people_list[k][j])
    
for k in range(N):
    max_num = max(max_num, people_list[i][k])
    
if max_num > people_list[i][j]:
    print("ANGRY")
else:
    print("HAPPY")

"""
a,*A=open(0)
_,a,b=map(int,a.split())
B=[l.split()[b-1]for l in A]
print('HAANPGPRYY'[int(B[a-1])<max(map(int,A[a-1].split()+B))::2])

ㄷㄷㄷ
"""
