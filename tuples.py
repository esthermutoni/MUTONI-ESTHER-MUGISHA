# 1. Display the second laptop brand
brands = ("Dell", "HP", "Lenovo", "Asus")
print(brands[1])

# 2. Print the second last item using negative indexing
devices = ("Dell", "HP", "Lenovo", "Asus")
print(devices[-2])

# 3. Replace "HP" with "Acer"
devices = ("Dell", "HP", "Lenovo", "Asus")
device_list = list(devices)
device_list[1] = "Acer"
devices = tuple(device_list)
print(devices)

# 4. Add "Microsoft" to the tuple
devices = ("Dell", "Acer", "Lenovo", "Asus")
device_list = list(devices)
device_list.append("Microsoft")
devices = tuple(device_list)
print(devices)

# 5. Iterate through the tuple
devices = ("Dell", "Acer", "Lenovo", "Asus", "Microsoft")
for item in devices:
    print(item)

# 6. Remove the first element from the tuple
devices = ("Dell", "Acer", "Lenovo", "Asus", "Microsoft")
device_list = list(devices)
device_list.pop(0)
devices = tuple(device_list)
print(devices)

# 7. Create a tuple of African countries using tuple()
countries = tuple(["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"])
print(countries)

# 8. Unpack the tuple
subjects = ("Math", "Science", "English")
sub1, sub2, sub3 = subjects
print(sub1)
print(sub2)
print(sub3)

# 9. Print the 2nd, 3rd, and 4th countries
countries = ("Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi")
print(countries[1:4])

# 10. Combine two tuples
boys = ("Brian", "Kevin", "Samuel")
girls = ("Grace", "Ruth", "Alice")
students = boys + girls
print(students)

# 11. Create a tuple of fruits and repeat it three times
fruits = ("Apple", "Banana", "Orange")
repeated_fruits = fruits * 3
print(repeated_fruits)

# 12. Count how many times 12 appears in the tuple
numbers = (4, 12, 6, 9, 12, 3, 12, 8, 5, 1)
occurrences = numbers.count(12)
print(occurrences)