nums = [int(i) for i in input().split()]
p = int(input())
res = [n ** p for n in nums]
print(*res, sep=' ')
