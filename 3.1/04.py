while len(s := input()) > 0:
    if len(s) > 3 and s[:-4:-1] == "@@@":
        continue
    elif len(s) > 2 and s[:2] == "##":
        print(s[2:])
    else:
        print(s)
