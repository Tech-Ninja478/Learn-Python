# String Operator

# Literal Assignment
first = "Aditya"
last = "Pachpute"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor Function
# pizza = str("Chicken Fiesta")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation

# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# Casting a Number to a String

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like the rock music from the " + decade + "s."
print(statement)  

# Multiline

multiline = '''
Hey! How are you doing?

All Good? I was just checking in!

                                        Let's meet someday
'''
print(multiline)
print("")

# Escaping Special Characters

sentence = 'I\'m back at work !\t Hey!\n\nWhere is this located at?'
print(sentence)
print("")

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("Good", "Okay"))
print(multiline)

print(len(multiline))
multiline += "                                                                 "
multiline = "                        " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.rstrip()))
print(len(multiline.lstrip()))
print("")

#Build a Menu
title = "menu".upper()
print(title.center(20, '='))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Hashbrown".ljust(16, ".") + "$2".rjust(4))

print("")

# String Index Values
print(first[1])
print(first[-1])
print(first[1:])

print(first.startswith("A"))
print(first.endswith("Z"))