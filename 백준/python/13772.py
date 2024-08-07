alphabet_list = [
    ["A", 1],
    ["B", 2],
    ["D", 1],
    ["O", 1],
    ["P", 1],
    ["Q", 1],
    ["R", 1]    
]

num = int(input())

for i in range(num):
    message = input()
    temp = 0

    for target in alphabet_list:
        char, j = target
        temp2 = message.count(char) * j
        temp += temp2
    print(temp)

"""
for i in[*open(0)][1:]:print(sum('ABBDOPQR'.count(s)for s in i))


?
"""
