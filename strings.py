# 1. Combine an integer and a string
student_age = 21
student_name = "Sarah"
message = f"{student_name} is {student_age} years old"
print(message)

# 2. Remove all spaces from a string
sentence = "      Welcome,       Africa!       "
no_spaces = sentence.replace(" ", "")
print(no_spaces)

# 3. Convert the string to uppercase
greeting = "Welcome, Africa!"
print(greeting.upper())

# 4. Replace the character 'A' with 'E'
greeting = "Welcome, Africa!"
updated_greeting = greeting.replace("A", "E")
print(updated_greeting)

# 5. Display the 2nd, 3rd, and 4th characters
text = "Python is cool"
print(text[1:4])

# 6. Fix the quotation marks in the string

# Method 1: Use single quotes around the string
quote = 'Every "Programmer" enjoys coding!'
print(quote)

# Method 2: Escape the double quotes
quote = "Every \"Programmer\" enjoys coding!"
print(quote)