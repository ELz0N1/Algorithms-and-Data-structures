import random


def HoareQuickSort(array, low, high):
    if high <= low:
        return

    i, j = low, high
    pivot = array[random.randint(low, high - 1)]

    while True:
        while i <= j and array[i] < pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i >= j:
            break

        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    HoareQuickSort(array, low, i)
    HoareQuickSort(array, j + 1, high)


def LomutoQuickSort(array, low, high):
    if high <= low:
        return

    i, j = low, low
    r = random.randint(low, high - 1)
    array[low], array[r] = array[r], array[low]
    pivot = array[low]

    for k in range(low + 1, high):
        if array[k] < pivot:
            array[k], array[j + 1], array[i] = array[j + 1], array[i], array[k]
            i += 1
            j += 1
        elif array[k] == pivot:
            array[j + 1], array[k] = array[k], array[j + 1]
            j += 1

    LomutoQuickSort(array, low, i)
    LomutoQuickSort(array, j + 1, high)


if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(10)]
    copy_nums = nums
    print(f'unsorted: {nums}')

    LomutoQuickSort(nums, 0, len(nums) - 1)
    HoareQuickSort(copy_nums, 0, len(nums) - 1)

    print(f'lomute: {nums}')
    print(f'hoare: {copy_nums}')
