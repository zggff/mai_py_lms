headings = [input() for _ in range(int(input()))]
find = input().lower()
for head in headings:
    if find in head.lower():
        print(head)
