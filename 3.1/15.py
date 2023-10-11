nums = [int(i) for i in input().split()]
a = nums[0]
for b in nums[1:]:
    while (r := a % b) > 0:
        a = b
        b = r
    a = b
print(a)
