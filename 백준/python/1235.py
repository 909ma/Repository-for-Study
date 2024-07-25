N = int(input())
students = []

for _ in range(N):
    students.append(input())

digit = len(students[0])
min_length = digit

for d in range(1, digit + 1):
    consecutive = []

    for student in students:
        consecutive.append(student[-d:])

    if len(set(consecutive)) == N:
        min_length = d
        break

    min_length = min(min_length, len(set(consecutive)))

print(min_length)
