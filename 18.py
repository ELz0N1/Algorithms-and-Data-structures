def is_operand(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')


def precedence(char):
    if char == '|':
        return 7
    elif char == '&':
        return 6
    # elif char == '<<' or char == '>>':
    #     return 5
    elif (char == '<' or char == '<=') or (char == '>' or char == '>='):
        return 5
    elif char == '==' or char == '!=':
        return 4
    elif char == '^':
        return 3
    elif char == '/' or char == '*' or char == '%':
        return 2
    elif char == '+' or char == '-':
        return 1
    else:
        return -1


def associativity(char):
    if char == '^':
        return 'R'
    return 'L'


def infix_to_postfix(expression):
    stack = []
    result = []

    for element in expression:
        if is_operand(element):
            result.append(element)
        elif element == '(':
            stack.append(element)
        elif element == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # pop '('
        else:
            while stack and (precedence(element) < precedence(stack[-1]) or
                             (precedence(element) == precedence(stack[-1]) and associativity(element) == 'L')):
                result.append(stack.pop())
            stack.append(element)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


if __name__ == "__main__":
    exp = "1-5^3*2"
    print(infix_to_postfix(exp))

    exp = "(1-5)&&(3*2)"
    print(infix_to_postfix(exp))
