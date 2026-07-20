# Create a list of students
students = ["Alice", "Brian", "Carol", "Daniel", "Evelyn"]

# Display the second item
print(students[1])  # Output: Brian

students = ["Alice", "Brian", "Carol", "Daniel", "Evelyn"]

# Update the first item
students[0] = "Grace"
print(students)

# Add a new item to the list
students.append("Frank")
print(students)

students = ["Alice", "Brian", "Carol", "Daniel", "Evelyn"]

# Insert a new item at the third position
students.insert(2, "Henry")
print(students)

students = ["Alice", "Brian", "Henry", "Carol", "Daniel", "Evelyn"]

# Remove the fourth item
del students[3]
print(students)

students = ["Alice", "Brian", "Henry", "Daniel", "Evelyn"]

# Print the last item using negative indexing
print(students[-1])

# Create a list of seven countries
places = ["Uganda", "Kenya", "Rwanda", "Tanzania", "Ethiopia", "Ghana", "Nigeria"]

# Display the 3rd, 4th, and 5th items
print(places[2:5])

# Original list
sports = ["Football", "Basketball", "Volleyball", "Tennis", "Rugby"]

# Make a copy of the list
sports_copy = list(sports)
print(sports_copy)

sports = ["Football", "Basketball", "Volleyball", "Tennis", "Rugby"]

# Loop through the list
for game in sports:
    print(game)

# List of fruits
fruits = ["Orange", "Apple", "Banana", "Mango", "Grapes"]

# Sort in ascending order
fruits.sort()
print("Ascending:", fruits)

# Sort in descending order
fruits.sort(reverse=True)
print("Descending:", fruits)

fruits = ["Orange", "Apple", "Banana", "Mango", "Grapes"]

# Print fruits containing the letter 'a'
for fruit in fruits:
    if "a" in fruit.lower():
        print(fruit)

# Combine two lists
male_names = ["David", "James", "Michael"]
female_names = ["Sarah", "Linda", "Rachel"]

all_names = male_names + female_names
print(all_names)