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


"""
s,*a=open(0);print(len({*a})//'`YFO'.find(s[-2]))


이게 무슨 코드야
"""
