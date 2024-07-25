import sys

n, m = map(int, sys.stdin.readline().split())

pokemon_dict = {}

for i in range(1, n+1):
    pokemon_name = sys.stdin.readline().rstrip()
    pokemon_dict[pokemon_name] = i

for _ in range(m):
    query = sys.stdin.readline().rstrip()

    if query.isdigit():
        idx = int(query)
        pokemon_name = list(pokemon_dict.keys())[idx-1]
        print(pokemon_name)
    else:
        idx = pokemon_dict.get(query)
        print(idx)
