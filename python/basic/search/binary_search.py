def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def test_binary_search():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert 0 == binary_search(array, 1)
    assert 3 == binary_search(array, 4)
    assert 6 == binary_search(array, 7)
    assert 8 == binary_search(array, 9)
    assert -1 == binary_search(array, 0)
    assert -1 == binary_search(array, 10)
