s = "   Aditya   "
f = s.lower()
c = list(f)
a=['a','e','i','o','u']
d=0
for i in c:
    if i in a:
        d=d+1
print(d)

print(s)
print(s.split())