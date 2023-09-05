for _ in range(int(input())):
    check = False
    temp_list = []
    size = int(input())
    for i in range(size):
        temp_list.append(input())
    temp_list2 = []
    for i in range(size):
        for j in range(size):
            if not (i == j):
                temp_list2.append(temp_list[i] + temp_list[j])

    for item in temp_list2:
        if item == item[::-1]:
            print(item)
            check = True
            break

    if not (check):
        print("0")
