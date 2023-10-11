from math import factorial

stack = []
for op in input().split():
    match op:
        case "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        case "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        case "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        case "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)
        case "~":
            a = stack.pop()
            stack.append(-a)
        case "!":
            a = stack.pop()
            stack.append(factorial(a))
        case "#":
            a = stack[-1]
            stack.append(a)
        case "@":
            c = stack.pop()
            b = stack.pop()
            a = stack.pop()
            stack.append(b)
            stack.append(c)
            stack.append(a)
        case n: stack.append(int(n))
print(stack[0])
