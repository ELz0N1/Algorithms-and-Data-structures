from random import choice
from string import ascii_lowercase


def countingSort(array, size, col, base):
    output = [0] * size
    count = [0] * base
    min_base = ord('a')

    for item in array:
        correct_index = min(len(item) - 1, col)
        letter = ord(item[-(correct_index + 1)]) - min_base
        count[letter] += 1

    for i in range(base - 1):
        count[i + 1] += count[i]

    for i in range(size - 1, -1, -1):
        item = array[i]
        correct_index = min(len(item) - 1, col)
        letter = ord(item[-(correct_index + 1)]) - min_base
        output[count[letter] - 1] = item
        count[letter] -= 1

    return output


def radixSort(array):
    size = len(array)

    max_col = len(max(array, key=len))

    for col in range(max_col):
        array = countingSort(array, size, col, 26)

    return array


def merge(arr, left, mid, right):
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]
    l, r, i = 0, 0, left

    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            arr[i] = left_arr[l]
            l += 1
        else:
            arr[i] = right_arr[r]
            r += 1
        i += 1

    while l < len(left_arr):
        arr[i] = left_arr[l]
        l += 1
        i += 1

    while r < len(right_arr):
        arr[i] = right_arr[r]
        r += 1
        i += 1


def merge_sort(arr, left=None, right=None):
    if left == None and right == None:
        left = 0
        right = len(arr)

    if right - left - 1:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


if __name__ == '__main__':
    lst = [''.join(choice(ascii_lowercase) for _ in range(10)) for _ in range(5)]
    copy_lst = lst
    print(f"Unsorted array: {lst}")

    radixSort(lst)
    merge_sort(copy_lst)

    print(f"LSD Sorted array: {lst}")
    print(f"Merge Sorted array: {copy_lst}")

    print(lst == copy_lst)
