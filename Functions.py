def hellow_world():
    print("Hello, World!")

hellow_world()

def sum(num1, num2):
    return num1 + num2

total = sum(5, 10)
print(total)

# Multiple arguments passing

def multiple(*args):
    print(args)
    print(type(args))

multiple('Aditya', 'Amogh', 45, 78.9)

# KWARGS

def keyword_args(**kwargs):
    print(kwargs)
    print(type(kwargs)) 

keyword_args(name='Aditya', age=20, city='Mumbai')