# Bill Split Calculator

# ── Input Section ──────────────────────────────────────────

# Get total bill amount
while True:
    bill_input = input("Enter the total bill amount (shs.): ")
    if bill_input.replace(".", "", 1).isdigit() and float(bill_input) > 0:
        bill_amount = float(bill_input)
        break
    else:
        print("Invalid input. Please enter a positive number.")

# Get number of people
while True:
    people_input = input("Enter the number of people splitting the bill: ")
    if people_input.isdigit() and int(people_input) > 0:
        num_people = int(people_input)
        break
    else:
        print("Invalid input. Please enter a positive whole number.")

# Get tip percentage
print("\nTip options:")
print("  1 → 10%")
print("  2 → 15%")
print("  3 → 20%")
print("  4 → Custom")

while True:
    tip_choice = input("Choose a tip option (1/2/3/4): ")

    if tip_choice == "1":
        tip_percent = 10
        break
    elif tip_choice == "2":
        tip_percent = 15
        break
    elif tip_choice == "3":
        tip_percent = 20
        break
    elif tip_choice == "4":
        custom_tip = input("Enter your custom tip percentage: ")
        if custom_tip.replace(".", "", 1).isdigit() and float(custom_tip) >= 0:
            tip_percent = float(custom_tip)
            break
        else:
            print("Invalid input. Please enter a positive number.")
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# ── Calculations ───────────────────────────────────────────

tip_amount    = bill_amount * (tip_percent / 100)
total_bill    = bill_amount + tip_amount
amount_each   = total_bill / num_people

# ── Output (formatted receipt) ─────────────────────────────

print(f"""
========================================
           BILL SPLIT RECEIPT
========================================
  Original Bill       : shs.{bill_amount:.2f}
  Tip ({tip_percent}%)           : shs.{tip_amount:.2f}
  Total Bill          : shs.{total_bill:.2f}
----------------------------------------
  Number of People    : {num_people}
  Each Person Pays    : shs.{amount_each:.2f}
========================================
""")