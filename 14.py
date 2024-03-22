from random import randint


def naiveImp(array, K):
    array.sort()
    return array[K]


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
        return kthQuickSort(array, j + 1, high, K)


if __name__ == '__main__':
    for j in range(101):
        nums = [randint(1, 100) for i in range(randint(1, 50))]

        result = kthQuickSort(nums, 0, len(nums), len(nums) // 2)
        naive_result = naiveImp(nums, len(nums) // 2)

        print(f"{result} == {naive_result}? {result == naive_result}")
