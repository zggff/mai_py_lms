# Таблица истинности 3
from typing import List, Dict
from itertools import product

PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def postfix_expression(expr, vars):
    stack = []
    result = []
    for i in expr.split():
        if i in vars:
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while len(stack) and PRIORITY[i] >= PRIORITY[stack[-1]]:
                result.append(stack.pop())
            stack.append(i)
    return result + stack[::-1]


def eval(expr: List[str], variables: Dict[str, int]) -> int:
    stack = []
    for e in expr:
        match e:
            case 'not':
                stack.append(not stack.pop())
            case 'and':
                a, b = stack.pop(), stack.pop()
                stack.append(a and b)
            case 'or':
                a, b = stack.pop(), stack.pop()
                stack.append(a or b)
            case '^':
                a, b = stack.pop(), stack.pop()
                stack.append(a != b)
            case '~':
                a, b = stack.pop(), stack.pop()
                stack.append(a == b)
            case '->':
                a, b = stack.pop(), stack.pop()
                stack.append(b <= a)
            case var:
                stack.append(variables[var])
    return stack.pop() * 1


def main():
    expr = input().replace('(', '( ').replace(')', ' )')
    vars = sorted({a for a in expr if a.isupper()})
    expr = postfix_expression(expr, vars)
    print(' '.join(vars), 'F')
    for p in product(range(2), repeat=len(vars)):
        v = {s: p[i] for i, s in enumerate(vars, 0)}
        print(' '.join(str(x) for x in p), eval(expr, v))


if __name__ == "__main__":
    main()
