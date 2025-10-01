s = "apple orange apple banana orange apple"

words = s.split()
d = {}

for s in words:
    d[s] = d.get(s, 0) + 1

c = max(d, key=d.get)
print(c)