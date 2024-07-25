letter = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
size = int(input())
num_list = map(int, input().split())
string = input()
char_list = []
for item in num_list:
    char_list.append(letter[item])

check_list = []
for item in string:
    check_list.append(item)

check_list.sort()
char_list.sort()
if check_list == char_list:
    print('y')
else:
    print('n')
