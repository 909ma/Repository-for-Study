box = int(input())
box_list = list(map(int, input().split()))
box_list = [0] + box_list + [0]
answer = 0

# 정면
answer += sum(box_list)

# 후면
answer += sum(box_list)

# 아랫면
answer += box

# 윗면
answer += box

# 옆면
for i in range(1, 1 + box):
    if box_list[i] - box_list[i - 1] > 0:
        answer += box_list[i] - box_list[i - 1]
    if box_list[i] - box_list[i + 1] > 0:
        answer += box_list[i] - box_list[i + 1] 

print(answer)
