def selection_sort(arr: list[int]):
    for i in range(len(arr)):
        # assume first element is the smallest element
        small_index = i

        # find the actual smallest element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[small_index]:
                small_index = j

        if arr[i] != arr[small_index]:
            # swap current element with smallest element in the remaining array
            arr[i], arr[small_index] = arr[small_index], arr[i]
    return arr


print(selection_sort([99, 1, 2, 9, 3]))
