def is_operand(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')


def precedence(char):
    if char == "||":
        return 10
    elif char == '&&':
        return 9
    elif char == '|':
        return 8
    elif char == '^':
        return 7
    elif char == '&':
        return 6
    elif char == "==" or char == "!=":
        return 5
    elif char == '+' or char == '-':
        return 3
    elif char == '/' or char == '*' or char == '%':
        return 2
    elif char == '!' or char == '~':
        return 1
    else:
        return -1


def associativity(char):
    if char == '!' or char == '~' or char == '&':
        return 'R'
    return 'L'


def infix_to_postfix(expression):
    stack = []
    result = []

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
            while stack and (precedence(element) < precedence(stack[-1]) or
                             (precedence(element) == precedence(stack[-1]) and associativity(element) == 'L')):
                result.append(stack.pop())
            stack.append(element)


    while stack:
        result.append(stack.pop())

    return ''.join(result)


if __name__ == "__main__":
    string = "( 1 - 5 ) ^ 3 * 2"
    exp = string.split()
    print(infix_to_postfix(exp))

    string = "9 + 3 * ( ( 2 % 5 ) - 1 ) ^ ( 6 + 7 * 4 ) - 8"
    exp = string.split()
    print(exp)
    print(infix_to_postfix(exp))

 
