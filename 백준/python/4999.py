import sys

line1 = sys.stdin.readline().rstrip()
line2 = sys.stdin.readline().rstrip()

size1 = len(line1)
size2 = len(line2)

if size1 >= size2:
    print("go")
else:
    print("no")
