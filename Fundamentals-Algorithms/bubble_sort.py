"""
Bubble Sort
"""


def bubble_sort(arr: list[int]):
    for passes in range(len(arr)):
        for j in range((len(arr) - 1) - passes):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([12, 25, 11, 34, 90, 22]))
"""
1st iteration:
passes = 0

j = 0
12, 25, 11, 34, 90, 22
j = 1
12, 25, 11, 34, 90, 22
12, 11, 25, 34, 90, 22
j = 2
12, 11, 25, 34, 90, 22
j = 3
12, 11, 25, 34, 90, 22
j = 4
12, 11, 25, 34, 22, 90

passes = 1
12, 11, 25, 34, 22
j = 0
11, 12, 25, 34, 22
j = 1
11, 12, 25, 34, 22
j = 2
11, 12, 25, 34, 22
j = 3
11, 12, 25, 22, 34

passes = 2
11, 12, 25, 22
j = 0
11, 12, 25, 22
j = 1
11, 12, 25, 22
j = 2
11, 12, 22, 25

passes = 3
11, 12, 22
j = 0
11, 12, 22
j = 1
11, 12, 22

passes = 4
11, 12
j = 0
11, 12

passes = 5
11

11, 12, 22, 25, 34, 90
"""
