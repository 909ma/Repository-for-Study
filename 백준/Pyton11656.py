string = input()
answer = []

for i in range(len(string)):
    answer.append(string[i:])

print("\n".join(sorted(answer)))


"""
s=input();print(*sorted(s[n:]for n in range(len(s))))


헐 이렇게도 줄여쓸 수 있었나
"""
