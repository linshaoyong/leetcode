def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less, greater = [], []
        for v in arr[1:]:
            if v <= pivot:
                less.append(v)
            else:
                greater.append(v)
    return quicksort(less) + [pivot] + quicksort(greater)


def test_sort():
    assert [1] == quicksort([1])
    assert [1, 2, 3] == quicksort([2, 1, 3])
    assert [1, 2, 3, 4, 5, 6] == quicksort([4, 6, 2, 1, 3, 5])
