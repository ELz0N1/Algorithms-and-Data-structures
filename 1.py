import random


def division(number: int, divider: int):
    if divider == 0:
        return "Сant be divided by zero"

    remainer, integer = 0, 0

    while number > 0:
        number -= divider
        integer += 1

    if number < 0:
        remainer = number + divider
    else:
        remainer = number

    return integer, remainer


if __name__ == "__main__":
    for i in range(10):
        A = random.randint(1, 1000000)
        B = random.randint(1, 1000000)
        print(f"number = {A}, divider = {B}, result = {division(A, B)}")
