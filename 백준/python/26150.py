N = int(input())
answer = ["0"] * N
temp_list = []
for i in range(N):
    message, num_i, num_d = input().split(' ')
    temp_list.append([int(num_i), num_d, message])

temp_list.sort()

for i in range(N):
    j = int(temp_list[i][1]) - 1
    # print(j, temp_list[i][2])
    answer[i] = temp_list[i][2][j].upper()

print(''.join(answer))

"""
for i,j,k in sorted(map(str.split,[*open(0)][1:]),key=lambda x:int(x[1])):print(end=i[int(k)-1].upper())

"""
