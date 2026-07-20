# 1. Print the value of the price
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 1200
}
print(product["price"])

# 2. Change the brand from "Dell" to "HP"
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 1200
}
product["brand"] = "HP"
print(product)

# 3. Add a new key/value pair
product = {
    "name": "Laptop",
    "brand": "HP",
    "price": 1200
}
product.update({"category": "Electronics"})
print(product)

# 4. Display all dictionary keys
product = {
    "name": "Laptop",
    "brand": "HP",
    "price": 1200,
    "category": "Electronics"
}
print(product.keys())

# 5. Display all dictionary values
product = {
    "name": "Laptop",
    "brand": "HP",
    "price": 1200,
    "category": "Electronics"
}
print(product.values())

# 6. Check whether the key "price" exists
product = {
    "name": "Laptop",
    "brand": "HP",
    "price": 1200,
    "category": "Electronics"
}

if "price" in product:
    print("Price key is available.")
else:
    print("Price key is missing.")

# 7. Loop through the dictionary
product = {
    "name": "Laptop",
    "brand": "HP",
    "price": 1200,
    "category": "Electronics"
}

for field, data in product.items():
    print(f"{field}: {data}")

# 8. Remove the "brand" key
product = {
    "name": "Laptop",
    "brand": "HP",
    "price": 1200,
    "category": "Electronics"
}
product.pop("brand")
print(product)

# 9. Clear all items in the dictionary
product = {
    "name": "Laptop",
    "price": 1200,
    "category": "Electronics"
}
product.clear()
print(product)

# 10. Copy a dictionary
employee = {
    "employee_name": "Grace",
    "department": "Finance",
    "location": "Kampala"
}
employee_duplicate = dict(employee)
print(employee_duplicate)

# 11. Nested dictionaries
employees = {
    "emp1": {
        "name": "Alice",
        "age": 28,
        "role": "Accountant"
    },
    "emp2": {
        "name": "Brian",
        "age": 31,
        "role": "Manager"
    }
}

print(employees["emp1"]["name"])
print(employees["emp2"]["role"])

for emp_id, info in employees.items():
    print(f"{emp_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")