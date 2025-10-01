a = [10, 10, 20, 10, 20, 30, 40, 50, 60]
b = set(a)
c = list(b)
d = {}
for i in a:
    d[i] = d.get(i, 0) + 1
print(d)


