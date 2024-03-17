import random


def divide(number: int, divider: int):
    if divider == 0:
        raise ValueError("Сan't be divided by zero")

    integer, remainer = 0, 0

    for digit in str(number):
        int_digit = 0
        current = int(digit) + remainer * 10

        for i in range(9, 0, -1):
            if current >= i * divider:
                current = current - (i * divider)
                int_digit += i

        integer = integer * 10 + int_digit
        remainer = current

    return integer, remainer


if __name__ == "__main__":
    nums = [(random.randint(2 ** 50, 2 ** 100), random.randint(2 ** 50, 2 ** 100)) for i in range(100)]

    for A, B in nums:
        print(f'{A}, {B}, {(A // B, A % B)} == {divide(A, B)}', (A // B, A % B) == divide(A, B))
