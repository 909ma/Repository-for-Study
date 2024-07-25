MatrixScale = int(input())
DefaultMatrix = []

for _ in range(MatrixScale):
    InputLine = input()
    DefaultMatrix.append(list(InputLine))

# 가로
RowCount = 0
TempMatrix = [row[:] for row in DefaultMatrix]
for i in range(MatrixScale):
    for j in range(MatrixScale - 1):
        if TempMatrix[i][j : j + 2] == [".", "."]:
            RowCount += 1
            TargetNumber = MatrixScale
            for k in range(j, MatrixScale):
                if TempMatrix[i][k] == ".":
                    pass
                elif TempMatrix[i][k] == "X":
                    TargetNumber = k
                    break
            for k in range(j, TargetNumber):
                TempMatrix[i][k] = "X"

# 세로
ColumnCount = 0
TempMatrix = [row[:] for row in DefaultMatrix]
for i in range(MatrixScale):
    for j in range(MatrixScale - 1):
        if TempMatrix[j][i] == "." and TempMatrix[j + 1][i] == ".":
            ColumnCount += 1
            TargetNumber = MatrixScale
            for k in range(j, MatrixScale):
                if TempMatrix[k][i] == ".":
                    pass
                elif TempMatrix[k][i] == "X":
                    TargetNumber = k
                    break
            for k in range(j, TargetNumber):
                TempMatrix[k][i] = "X"

print(RowCount, ColumnCount)

"""
DefaultMatrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

# 얕은 복사 (객체를 공유)
TempMatrix_shallow = DefaultMatrix

# 깊은 복사 (새로운 객체 생성)
TempMatrix_deep = [row[:] for row in DefaultMatrix]

DefaultMatrix[0][0] = "x"

print(DefaultMatrix)
print(TempMatrix_shallow)  # 얕은 복사
print(TempMatrix_deep)     # 깊은 복사
----------------------------------------------------------------------------------------------------------
얕은 복사(shallow copy)와 깊은 복사(deep copy)는 데이터 구조의 복사 방법을 나타내는 두 가지 주요 개념입니다. 이를 이해하기 위해 다양한 자료형을 예시로 들어 설명하겠습니다.

1. **리스트 (List)**:
   ```python
   original_list = [1, [2, 3], 4]
   
   # 얕은 복사
   shallow_copied_list = original_list.copy()  # 또는 shallow_copied_list = original_list[:]
   shallow_copied_list[1][0] = 999
   print(original_list)  # [1, [999, 3], 4]

   # 깊은 복사
   import copy
   deep_copied_list = copy.deepcopy(original_list)
   deep_copied_list[1][0] = 888
   print(original_list)  # [1, [999, 3], 4]
   ```

2. **딕셔너리 (Dictionary)**:
   ```python
   original_dict = {'a': 1, 'b': {'x': 2, 'y': 3}}
   
   # 얕은 복사
   shallow_copied_dict = original_dict.copy()
   shallow_copied_dict['b']['x'] = 999
   print(original_dict)  # {'a': 1, 'b': {'x': 999, 'y': 3}}

   # 깊은 복사
   import copy
   deep_copied_dict = copy.deepcopy(original_dict)
   deep_copied_dict['b']['y'] = 888
   print(original_dict)  # {'a': 1, 'b': {'x': 999, 'y': 3}}
   ```

3. **세트 (Set)**:
   ```python
   original_set = {1, 2, {3, 4}}
   
   # 얕은 복사
   # 얕은 복사는 세트에 대해 의미 없는 경우가 많아 예시를 들기 어려울 수 있습니다.

   # 깊은 복사
   # 깊은 복사 역시 세트에 대해 의미 없는 경우가 많아 예시를 들기 어려울 수 있습니다.
   ```

4. **튜플 (Tuple)**:
   ```python
   original_tuple = (1, [2, 3], 4)
   
   # 얕은 복사
   shallow_copied_tuple = list(original_tuple)
   shallow_copied_tuple[1][0] = 999
   print(original_tuple)  # (1, [999, 3], 4)

   # 깊은 복사
   import copy
   deep_copied_tuple = copy.deepcopy(original_tuple)
   deep_copied_tuple[1][1] = 888
   print(original_tuple)  # (1, [999, 3], 4)
   ```

각 예시에서 볼 수 있듯이 얕은 복사는 원본 데이터와 복사본이 동일한 객체를 참조하여 내부 구조가 바뀔 때 문제가 발생할 수 있습니다. 반면 깊은 복사는 원본 데이터와 완전히 별개의 객체를 생성하여 데이터 무결성을 보존합니다. 중첩된 데이터 구조에서는 깊은 복사가 더 안전하게 작업할 수 있는 방법입니다.

"""
"""
n, *a = open(0)
f = lambda x: sum(sum(1 < len(j) for j in "".join(i).strip().split("X")) for i in x)
print(f(a), f(zip(*a)))

이렇게도 짜네
"""
