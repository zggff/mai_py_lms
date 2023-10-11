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
        case n: stack.append(int(n))
print(stack[0])
