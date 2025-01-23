# Dictionaries

band = {
    "vocal": "Plant",
    "guitar": "Page"
}

band2 = dict(vocal = "Plant", guitar = "Page")

print(band)
print(band2)
print(type(band))
print(len(band2))

# Access item in a dictionary

print(band["vocal"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# Verify a key exists or not

print("guitar" in band)
print("triangle" in band)

# Change Values 

band["vocal"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

#Remove Values

print(band.pop("bass"))
print(band)

# Delete and Remove Item

band["drums"] = "Bonham"
del band["drums"]
print (band)

band2.clear()
print(band2)

del band2

# Copy Dictionaries

band2 = band.copy()
band2["drums"] = "Aditya"
print("Good Copy!")
print(band)
print(band2)

# Copy using dict() constructor function

band3 = dict(band2)
print("Good Copy!")
print(band3)

# Nested Dictionaries

member1 = {
    "name": "Plant",
    "instrument": "Guitar"
}

member2 = {
    "name": "Page",
    "instrument": "Vocals"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])