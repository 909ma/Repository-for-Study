from collections import defaultdict

word = input()

counts = defaultdict(int)
for char in word:
    counts[char] += 1

for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    print(counts[char], end=' ')
