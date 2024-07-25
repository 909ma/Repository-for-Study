def calculate_area(points):
    area = set()
    for point in points:
        for i in range(point[0], point[2]):
            for j in range(point[1], point[3]):
                area.add((i, j))
    return len(area)

points = []
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    points.append((x1, y1, x2, y2))

result = calculate_area(points)
print(result)
