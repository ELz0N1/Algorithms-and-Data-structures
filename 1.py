import random


def divide(number: int, divider: int):
    if divider == 0:
        raise ValueError("Сan't be divided by zero")

    integer, remainer = 0, 0

    for digit in str(number):
        int_digit = 0
        current = int(digit) + remainer * 10

        while current >= divider:
            current -= divider
            int_digit += 1

        integer = integer * 10 + int_digit
        remainer = current

    return integer, remainer


if __name__ == "__main__":
    nums = [(random.randint(2 ** 50, 2 ** 100), random.randint(2 ** 50, 2 ** 100)) for i in range(100)]

    for A, B in nums:
        assert (A // B, A % B) == divide(A, B)

    print("All tests passed")

