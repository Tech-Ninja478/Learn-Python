s = "he@llo#2025!"
b = list(s)
a = ["!", "@", "#", "$", "^", "&", "*"]


for i in b:
    if i in a:
        b.remove(i)
    
print(b)