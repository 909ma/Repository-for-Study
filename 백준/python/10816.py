from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
card_count = defaultdict(int)

for card in cards:
    card_count[card] += 1

for target in targets:
    print(card_count[target], end=' ')
