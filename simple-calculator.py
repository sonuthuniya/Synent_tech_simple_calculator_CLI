def calculator():
    while True:
        print("\n=== Simple Calculator CLI ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"Result: {num1 + num2}")
                elif choice == "2":
                    print(f"Result: {num1 - num2}")
                elif choice == "3":
                    print(f"Result: {num1 * num2}")
                elif choice == "4":
                    if num2 != 0:
                        print(f"Result: {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        elif choice == "5":
            print("Exiting Calculator... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    calculator()

