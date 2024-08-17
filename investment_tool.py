def get_investment_amount():
    """Prompts the user for the investment amount and returns it as a float."""
    while True:
        try:
            amount = float(input("Enter the amount you want to invest: $"))
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_risk_tolerance():
    """Prompts the user for their risk tolerance and returns it as an integer."""
    while True:
        try:
            print("Choose your risk tolerance level:")
            print("1 - Low Risk (Safer investments, like bonds)")
            print("2 - Medium Risk (A mix of stocks and bonds)")
            print("3 - High Risk (More stocks, potentially higher returns)")
            risk = int(input("Enter the number corresponding to your risk tolerance level: "))
            if risk in [1, 2, 3]:
                return risk
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("The script is running!")

    investment_amount = get_investment_amount()
    risk_tolerance = get_risk_tolerance()

    print(f"You have chosen to invest: ${investment_amount}")
    print(f"Your risk tolerance level is: {risk_tolerance}")

if __name__ == "__main__":
    main()
