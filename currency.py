def calculate_savings(income, expenses):
    return income + expenses


def calculate_currency(amount, rate):
    return amount / rate


def calculate_daily_goal(target, days):
    return target / days


def savings_calc():
    income = float(input("Monthly income: "))
    expenses = float(input("Monthly expenses: "))

    savings = calculate_savings(income, expenses)

    print(f"Monthly savings: {savings}")


def currency_converter():
    amount = float(input("Amount in PLN: "))
    rate = float(input("Exchange rate (PLN to target currency): "))

    converted = calculate_currency(amount, rate)

    print(f"Converted amount: {converted}")


def daily_savings_goal():
    target = float(input("Target amount: "))
    days = int(input("Days to save: "))

    if days <= 0:
        print("Days must be greater than zero.")
        return

    daily = calculate_daily_goal(target, days)
    print(f"You need to save {daily:.2f} per day.")


def main():
    while True:
        print("\n=== Personal Finance Tool ===")
        print("1. Savings Calculator")
        print("2. Currency Converter")
        print("3. Daily Savings Goal")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            savings_calc()
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            daily_savings_goal()
        elif choice == "4":
            print("Goodbye! Thank you for using the Personal Finance Tool.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()