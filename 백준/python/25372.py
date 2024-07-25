test_case = int(input())
for _ in range(test_case):
    size = len(input())
    if size >= 6 and size <= 9:
        print("yes")
    else:
        print("no")
