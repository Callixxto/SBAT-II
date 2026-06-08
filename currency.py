def savings_calc():
    income = float(input("Monthly income: "))
    expenses = float(input("Monthly expenses: "))

    savings = income - expenses

    print(f"Monthly savings: {savings}")


def currency_converter():
    amount = float(input("Amount in PLN: "))
    rate = float(input("Exchange rate (PLN to target currency): "))

    converted = amount / rate

    print(f"Converted amount: {converted}")

def new_function():
    print("This is a new function added to the code.")


def main():
    while True:
        print("\n=== Personal Finance Tool ===")
        print("1. Savings Calculator")
        print("2. Currency Converter")
        print("3. Quit the application.")

        choice = input("Choose an option: ")

        if choice == "1":
            savings_calc()
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            print("Goodbye! Thank you for using the Personal Finance Tool.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()