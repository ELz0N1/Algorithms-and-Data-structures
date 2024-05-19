from random import randint


def kth(array, k):
    if len(array) == 1:
        return array[0]

    pivot = randint(0, len(array) - 1)
    p = partition(array, pivot)

    if p == k:
        return array[p]
    elif p + 1 > k:
        return kth(array[:p], k)
    else:
        return kth(array[p + 1:], k - p - 1)


def partition(array, pivot_index):
    n = len(array) - 1
    pivot = array[pivot_index]
    array[pivot_index], array[n] = array[n], array[pivot_index]
    store_index = 0
    for i in range(n):
        if array[i] < pivot:
            array[store_index], array[i] = array[i], array[store_index]
            store_index += 1
    array[store_index], array[n] = array[n], array[store_index]
    return store_index


def tests():
    array = [41, 6, 22, 46, 53, 26, 76, 92, 37, 82, 79, 1, 60, 84, 91, 53, 7, 84]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [85, 62, 64, 16, 19, 19, 22, 85, 55]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [94, 15, 32]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [81, 59, 43, 87, 14, 7, 97, 18, 1, 66, 18, 83, 24]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [2, 35, 29, 39, 64, 59, 3, 17]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [4, 20, 50, 46, 82, 90, 1, 85, 48, 94]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [27, 76, 99, 32, 70, 59, 64, 60, 82, 14, 56]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [28, 14, 52, 53, 28, 97, 36, 2, 69, 84, 15, 65, 37, 60, 94, 24, 79]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [46, 1, 48, 21, 48, 51, 39, 85, 9, 42, 97, 1, 3, 43, 93, 19]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    array = [45, 65, 87, 3, 26, 95, 65, 58]
    assert kth(array, len(array) // 2) == sorted(array)[len(array) // 2]

    print("All tests passed!")


if __name__ == '__main__':
    tests()
