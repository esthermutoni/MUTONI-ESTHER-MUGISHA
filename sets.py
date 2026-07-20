# 1. Create a set of 3 favorite snacks using the set() constructor
snacks = set(["chips", "cookies", "popcorn"])
print(snacks)

# 2. Add two more items to the snacks set
snacks = {"chips", "cookies", "popcorn"}
snacks.update(["nuts", "biscuits"])
print(snacks)

# 3. Check whether "blender" exists in the set
appliances = {"toaster", "blender", "mixer", "freezer"}

if "blender" in appliances:
    print("Blender is available in the set")
else:
    print("Blender is not available")

# 4. Remove "toaster" from the set
appliances = {"toaster", "blender", "mixer", "freezer"}
appliances.discard("toaster")
print(appliances)

# 5. Iterate through the set
appliances = {"blender", "mixer", "freezer"}
for appliance in appliances:
    print(appliance)

# 6. Add all items from a list into a set
fruit_set = {"mango", "orange", "grape", "pear"}
extra_fruits = ["pineapple", "papaya"]
fruit_set.update(extra_fruits)
print(fruit_set)

# 7. Merge two sets together
scores = {70, 85, 90}
students = {"Alice", "Brian", "Cathy"}
merged_set = scores | students
print(merged_set)