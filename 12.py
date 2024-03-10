import random


def LomutoQuickSort(array, low, high):
    if high <= low: return

    l, h = low, low
    pivot_idx = random.randint(low, high - 1)
    array[low], array[pivot_idx] = array[pivot_idx], array[low]
    pivot = array[low]

    for c in range(low + 1, high):
        if array[c] < pivot:
            array[c], array[h + 1], array[l] = array[h + 1], array[l], array[c]
            l += 1
            h += 1
        elif array[c] == pivot:
            array[h + 1], array[c] = array[c], array[h + 1]
            h += 1

    LomutoQuickSort(array, low, l)
    LomutoQuickSort(array, h + 1, high)


def HoareQuickSort(array, low, high):
    if high <= low: return

    i, j = low, high
    pivot = array[random.randint(low, high - 1)]

    while True:
        while i <= j and array[i] < pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i >= j: break

        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    HoareQuickSort(array, low, i)
    HoareQuickSort(array, j + 1, high)


if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(10)]
    copy_nums = nums
    print(f'unsorted: {nums}')

    LomutoQuickSort(nums, 0, len(nums) - 1)
    HoareQuickSort(copy_nums, 0, len(nums) - 1)

    print(f'lomute: {nums}')
    print(f'hoare: {copy_nums}')
