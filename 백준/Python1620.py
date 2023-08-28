import sys

n, m = map(int, sys.stdin.readline().split())
pokemon_dict = {}

for i in range(1, n + 1):
    a = sys.stdin.readline().rstrip()
    pokemon_dict[i] = a
    pokemon_dict[a] = i

for i in range(m):
    index = sys.stdin.readline().rstrip()
    if index.isdigit():
        print(pokemon_dict[int(index)])
    else:
        print(pokemon_dict[index])
