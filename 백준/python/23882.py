change_count = 0

N, K = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))

i = 0
is_search = False

while True:
    target_num = num_list[N-1-i]
    if N-1-i == 0:
        break
    next_max_num = max(num_list[:N-1-i])
    if target_num < next_max_num:
        temp_index = num_list.index(next_max_num)
        num_list[temp_index] = target_num
        num_list[N-1-i] = next_max_num
        change_count += 1
    i += 1
    if change_count == K:
        print(' '.join(map(str, num_list)))
        is_search = True
        break
if not is_search:
    print(-1)


"""
a, b = map(int, input().split())
lst = list(map(int, input().split()))

count = 0

for i in range(a-1, 0, -1):
    max_index = lst.index(max(lst[:i+1]))
    if max_index == i:
        continue
    else:
        lst[i], lst[max_index] = lst[max_index], lst[i]
        count += 1

    if count == b:
        print(*lst)
        break

if count < b:
    print(-1)


"""
