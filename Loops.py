value = 0

# While Loop

# while value < 10:
#     print(value)
#     value += 1

# while value < 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# For Loop

names = ["John", "Eric", "Jessica"]

# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Eric":
#         break
#     print(x)

# for x in range(2, 4):
#     print(x)

for x in range(5, 101, 5):
    print(x)

names = ["John", "Eric", "Jessica"]
activities = ["running", "dancing", "singing"]

# for name in names:
#     for activity in activities:
#         print(name + " likes " + activity + ".")

for activity in activities:
    for name in names:
        print(name + " likes " + activity + ".")