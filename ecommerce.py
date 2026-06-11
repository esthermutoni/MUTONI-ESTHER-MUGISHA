USERS = {
	"admin": {"password": "admin123", "role": "Admin"},
	"customer": {"password": "cust123", "role": "Customer"},
	"cashier": {"password": "cash123", "role": "Cashier"},
}


def get_positive_number(prompt):
	while True:
		value = input(prompt)
		try:
			number = float(value)
			if number > 0:
				return number
			print("Please enter a number greater than zero.")
		except ValueError:
			print("Invalid input. Please enter a number.")


def login():
	print("=== E-COMMERCE LOGIN ===")
	username = input("Username: ").strip().lower()
	password = input("Password: ").strip()

	if username in USERS:
		if password == USERS[username]["password"]:
			print(f"Login successful. Welcome, {USERS[username]['role']}!")
			return USERS[username]["role"]
		else:
			print("Wrong password.")
	else:
		print("Unknown username.")

	return None


def get_discount(subtotal):
	if subtotal >= 100000:
		return 20
	else:
		if subtotal >= 50000:
			return 10
		else:
			if subtotal >= 20000:
				return 5
			else:
				return 0


def get_tax_rate(location):
	location = location.strip().lower()
	if location == "kampala":
		return 18
	else:
		if location == "nairobi":
			return 16
		else:
			if location == "dar es salaam":
				return 15
			else:
				return 12


def get_coupon_discount(coupon_code):
	coupon_code = coupon_code.strip().upper()
	if coupon_code == "":
		return 0
	else:
		if coupon_code == "SAVE10":
			return 10
		else:
			if coupon_code == "VIP20":
				return 20
			else:
				print("Invalid coupon code. No coupon discount applied.")
				return 0


def checkout():
	print("\n CHECKOUT ")
	subtotal = get_positive_number("Enter subtotal amount: ")
	location = input("Enter location (Kampala/Nairobi/Dar es Salaam/Other): ")
	coupon_code = input("Enter coupon code if any: ")

	base_discount = get_discount(subtotal)
	coupon_discount = get_coupon_discount(coupon_code)
	tax_rate = get_tax_rate(location)

	discount_amount = subtotal * (base_discount / 100)
	after_discount = subtotal - discount_amount
	coupon_amount = after_discount * (coupon_discount / 100)
	taxable_amount = after_discount - coupon_amount
	tax_amount = taxable_amount * (tax_rate / 100)
	total = taxable_amount + tax_amount

	print("\n=== RECEIPT ===")
	print(f"Subtotal: shs. {subtotal:.2f}")
	print(f"Base discount: {base_discount}% = shs. {discount_amount:.2f}")
	print(f"Coupon discount: {coupon_discount}% = shs. {coupon_amount:.2f}")
	print(f"Tax rate: {tax_rate}% = shs. {tax_amount:.2f}")
	print(f"Total to pay: shs. {total:.2f}")


def main():
	role = login()

	if role is None:
		print("Access denied.")
	else:
		if role == "Admin":
			print("Admin access: you can view reports and process checkout.")
			checkout()
		else:
			if role == "Cashier":
				print("Cashier access: you can process checkout only.")
				checkout()
			else:
				if role == "Customer":
					print("Customer access: you can place an order.")
					checkout()
				else:
					print("No access level found.")


if __name__ == "__main__":
	main()
