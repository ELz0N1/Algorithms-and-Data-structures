from random import randint


def kthQuickSort(array, low, high, K):
    if len(array) == 1: return array[low]

    i, j = low, high - 1
    pivot = array[randint(low, high - 1)]

    while True:
        while i <= j and array[i] < pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i >= j: break

        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    if (array[j] == pivot and j == K) or (array[i] == pivot and i == K):
        return pivot

    if i > K:
        return kthQuickSort(array, low, i, K)
    else:
        return kthQuickSort(array, i, high, K)


def tests():
    array = [41, 6, 22, 46, 53, 26, 76, 92, 37, 82, 79, 1, 60, 84, 91, 53, 7, 84]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 53

    array = [85, 62, 64, 16, 19, 19, 22, 85, 55]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 55

    array = [94, 15, 32]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 32

    array = [81, 59, 43, 87, 14, 7, 97, 18, 1, 66, 18, 83, 24]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 43

    array = [2, 35, 29, 39, 64, 59, 3, 17]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 35

    array = [4, 20, 50, 46, 82, 90, 1, 85, 48, 94]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 50

    array = [27, 76, 99, 32, 70, 59, 64, 60, 82, 14, 56]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 60

    array = [28, 14, 52, 53, 28, 97, 36, 2, 69, 84, 15, 65, 37, 60, 94, 24, 79]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 52

    array = [46, 1, 48, 21, 48, 51, 39, 85, 9, 42, 97, 1, 3, 43, 93, 19]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 43

    array = [45, 65, 87, 3, 26, 95, 65, 58]
    assert kthQuickSort(array, 0, len(array), len(array) // 2) == 65

    print("All tests passed!")


if __name__ == '__main__':
    tests()
