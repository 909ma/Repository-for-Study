num = input()
num_list = []
for i in num:
    num_list.append(int(i))

num_list.sort(reverse=True)
if sum(num_list) % 3 != 0 or num_list[-1] != 0:
    print(-1)
else:
    result = ''.join(map(str, num_list))
    print(result)


"""
print([x:=int("".join(sorted(input())[::-1])),-1][x%30>0])


와 똑똑하네
"""
