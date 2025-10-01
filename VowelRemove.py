s = "Beautiful"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for letters in s:
    if letters in vowels:
        s = s.replace(letters, "")
    
print(s)