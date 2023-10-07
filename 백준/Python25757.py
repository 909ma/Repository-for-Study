times, Game = input().split()
player = set()
for _ in range(int(times)):
    player.add(input())
if Game == "Y":
    X = 1
elif Game == "F":
    X = 2
else:
    X = 3
print(len(player) // X)
