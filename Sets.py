nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

# No dupicate allowed

nums = {1, 2, 2, 4}
print(nums)

# True id a dupe of 1 and False is a dupe of 0

nums2 = {1, True, 2, 3, False, 0}
print(nums2)

# Check a value in Set

print(2 in nums)

# Add new values to the Set
nums2.add(5)
print(nums2)

# Add value from one set to another

morenums = {6, 7, 8, 9 , 10}
nums2.update(morenums)
print(nums2)