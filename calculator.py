# Menu-driven calculator using functions

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


while True:
    print("\n===== Calculator Menu =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    option = input("Select an option (1-5): ")

    if option == "5":
        print("Calculator closed. See you next time!")
        break

    first_value = float(input("Enter first value: "))
    second_value = float(input("Enter second value: "))

    if option == "1":
        answer = addition(first_value, second_value)
        print(f"Result: {answer}")

    elif option == "2":
        answer = subtraction(first_value, second_value)
        print(f"Result: {answer}")

    elif option == "3":
        answer = multiplication(first_value, second_value)
        print(f"Result: {answer}")

    elif option == "4":
        answer = division(first_value, second_value)

        if isinstance(answer, str):
            print(answer)
        else:
            print(f"Result: {answer}")

    else:
        print("Invalid selection. Please choose a number from 1 to 5.")