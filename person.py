class Person:
    def __init__(self, given_name, family_name, years_old, contact_email):
        self.given_name = given_name
        self.family_name = family_name
        self.years_old = years_old
        self.contact_email = contact_email

    def display_details(self):
        print("User Information")
        print(f"Name: {self.given_name} {self.family_name}")
        print(f"Age: {self.years_old}")
        print(f"Email: {self.contact_email}")

    def welcome(self):
        print(f"Hello, {self.given_name}! Welcome.")


# Create person objects
person_a = Person("James", "Brown", 28, "james@gmail.com")
person_b = Person("Linda", "Wilson", 31, "linda@gmail.com")
person_c = Person("David", "Taylor", 24, "david@gmail.com")

# Display details and greetings
person_a.display_details()
person_a.welcome()

print()

person_b.display_details()
person_b.welcome()

print()

person_c.display_details()
person_c.welcome()