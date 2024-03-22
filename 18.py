def is_operand(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')


def get_precedence(operation):
    precedence = {
        '(': 0,
        ')': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '&': 3,
        '|': 3,
        '^': 3,
        '<<': 4,
        '>>': 4,
        '<': 5,
        '<=': 5,
        '>': 5,
        '>=': 5,
        '==': 6,
        '!=': 6,
        '&&': 7,
        '||': 8,
        '!': 9,
        '~': 9
    }
    return precedence[operation]


def associativity(operation):
    if operation == '!' or operation == '~' or operation == '&':
        return 'R'
    return 'L'


def infix_to_postfix(string):
    stack = []
    result = []

    expression = string.split()
    expression.reverse()
    while expression:
        element = expression.pop()
        if is_operand(element):
            result.append(element)

        elif element == '(':
            stack.append(element)

        elif element == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        else:
            while stack and (get_precedence(element) <= get_precedence(stack[-1]) or
                             (get_precedence(element) == get_precedence(stack[-1]) and associativity(element) == 'L')):
                result.append(stack.pop())
            stack.append(element)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


if __name__ == "__main__":
    assert infix_to_postfix("( 1 - 5 ) ^ 3 * 2") == "15-3^2*"
    assert infix_to_postfix("2 * 1 / 1 * 2 + 1") == "21*1/2*1+"
    assert infix_to_postfix("4 * ( 1 + 9 )") == "419+*"
    assert infix_to_postfix("6 * ( 0 + 7 ) / 2") == "607+*2/"
    assert infix_to_postfix("2 * ( ( 9 + 6 ) / 3 )") == "296+3/*"
    assert infix_to_postfix("c | ( b & a )") == "cba&|"
    assert infix_to_postfix("! x | ( y & z )") == "x!yz&|"

    print("All tests passed")
