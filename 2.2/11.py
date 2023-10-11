n = [int(i) for i in input()]
print(''.join(map(str, sorted([sum(n[1:]), sum(n[:2])], reverse=True))))
