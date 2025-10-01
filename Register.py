d = {1:["Saurabh","Male","1234567890"], 2:["Jai","Male","7418529638"], 3:["Ayaan","Male","8794563217"]}

reg = int(input("Enter the number:"))

name = input("Enter the name:")
gender = input("Enter the gender:")

cont = input("Enter the Contact No:")
a = []
a.append(name)
a.append(gender)
a.append(cont)
d[reg] = a
print(d)