def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp, position = arr[i], i - 1
        while position >= 0:
            if arr[position] > tmp:
                arr[position + 1] = arr[position]
                position -= 1
            else:
                break
        arr[position + 1] = tmp
    return arr


def test_sort():
    assert [1] == insertion_sort([1])
    assert [1, 2, 3] == insertion_sort([2, 1, 3])
    assert [1, 2, 3, 4, 5, 6] == insertion_sort([4, 6, 2, 1, 3, 5])
