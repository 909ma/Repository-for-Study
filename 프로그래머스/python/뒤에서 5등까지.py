def solution(num_list):
    answer = sorted(num_list)
    return answer[0:5]


print(solution([12, 4, 15, 46, 38, 1, 14]))


"""
파이썬에서 `.sort()`, `sort()`, 그리고 `sorted()`는 모두 리스트의 요소를 정렬하는 데 사용되는 메서드나 함수입니다. 그러나 각각의 차이점이 있습니다:

1. `.sort()`: 이 메서드는 리스트 자체를 정렬하며, 새로운 정렬된 리스트를 생성하지 않습니다. 즉, 원래의 리스트를 변경하고, 반환 값은 `None`입니다. 예를 들어:

```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # [1, 2, 3]
```

2. `sort()`: 이것은 리스트 객체의 메서드입니다. 리스트 이름 뒤에 붙여서 호출합니다. 반환 값은 `None`입니다. 따라서 `my_list.sort()`와 같이 사용합니다.

3. `sorted()`: 이 함수는 리스트나 다른 반복 가능한(iterable) 객체를 인자로 받아서 정렬된 새로운 리스트를 반환합니다. 원본 리스트를 변경하지 않습니다. 예를 들어:

```python
my_list = [3, 1, 2]
sorted_list = sorted(my_list)
print(sorted_list)  # [1, 2, 3]
print(my_list)  # [3, 1, 2] (원본 리스트는 변경되지 않음)
```

따라서 선택하는 것은 상황에 따라 다릅니다. 원본 리스트를 변경하려면 `.sort()`를 사용하고, 원본 리스트를 유지하면서 정렬된 새로운 리스트를 얻으려면 `sorted()` 함수를 사용하세요.


이런 디테일이~
"""
