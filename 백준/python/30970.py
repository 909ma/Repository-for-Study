N = int(input())

quality = []
quantity = []

for _ in range(N):
    qual, quan = map(int, input().split(' '))
    quality.append([qual, quan])
    quantity.append([quan, qual])

quality.sort(key=lambda x: (-x[0], x[1]))
quantity.sort(key=lambda x: (x[0], -x[1]))

# print(quality)
# print(quantity)

print(f"{quality[0][0]} {quality[0][1]} {quality[1][0]} {quality[1][1]}")
print(f"{quantity[0][1]} {quantity[0][0]} {quantity[1][1]} {quantity[1][0]}")
