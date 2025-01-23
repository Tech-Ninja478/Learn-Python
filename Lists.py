users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users +=["Jason"]
print(users)

users.extend(["Percy", "Grover"])
print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users.remove("Bob")
print(users)

pop = users.pop()
print(users)
print("Popped item is " + pop)

del users[0]
print(users)

# Adding a lower case name to the string and sorting
users[1:2] = ["dave"]
print(users)

users.sort()
print(users) # dave is printed at the end beacuse it's in lower case

# To solve this problem we perform the following function
users.sort(key=str.lower)
print(users)

nums = [34, 25, 87, 56, 42]
print(nums)

nums.reverse()
print(nums)

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)
print(nums)