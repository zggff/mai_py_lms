ns = [f"{int(i):0b}" for i in input().split()]
ns = [{"digits": len(i), "units": i.count(
    "1"), "zeros": i.count("0")} for i in ns]
print(ns)
