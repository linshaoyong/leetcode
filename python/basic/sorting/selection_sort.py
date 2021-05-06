def selection_sort(arr):

    for i in range(len(arr)):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


def test_sort():
    assert [1] == selection_sort([1])
    assert [1, 2, 3] == selection_sort([2, 1, 3])
    assert [1, 2, 3, 4, 5, 6] == selection_sort([4, 6, 2, 1, 3, 5])
