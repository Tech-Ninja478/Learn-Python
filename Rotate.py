s = input("Enter the String: ")

n = int(input("Enter the number of times to rotate: "))

if n > len(s):
    print("Invalid Input")
    exit()

print(s[-n:] + s[:-n])