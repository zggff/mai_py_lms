while (s := input()) != "":
    if "#" in s:
        s = s[:s.find("#")]
        if len(s) > 0:
            print(s)
    else:
        print(s)
