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