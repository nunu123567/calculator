import math

def ask_number():
    while True:
        value = input("Give a number: ")
        try:
            return float(value)
        except ValueError:
            print("This input is invalid.")

def print_result(value):
    if isinstance(value, float) and value.is_integer():
        print("The result is:", int(value))
    else:
        print("The result is:", value)

print("Calculator")

number1 = ask_number()
number2 = ask_number()

while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5)sin(number1/number2)")
    print("(6)cos(number1/number2)")
    print("(7)Change numbers")
    print("(8)Quit")
    print("Current numbers:",
          int(number1) if number1.is_integer() else number1,
          int(number2) if number2.is_integer() else number2)

    choice = input("Please select something (1-6): ")

    if choice == "1":
        print_result(number1 + number2)

    elif choice == "2":
        print_result(number1 - number2)

    elif choice == "3":
        print_result(number1 * number2)

    elif choice == "4":
        if number2 == 0:
            print("Division by zero is not allowed.")
        else:
            print_result(number1 / number2)
