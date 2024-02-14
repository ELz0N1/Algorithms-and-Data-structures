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
    print(division(0, 2))
    print(division(3492, 10))
    print(division(845967868, 5))
