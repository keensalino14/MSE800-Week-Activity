from database import (
    create_database,
    save_customer,
    save_transaction
)


# =========================
# CUSTOMER CLASS
# =========================

class Customer:

    def __init__(
        self,
        customer_id,
        full_name,
        email,
        phone,
        address
    ):
        self.customer_id = customer_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address


# =========================
# CURRENCY CLASS
# =========================

class Currency:

    def __init__(self, currency_id, code, name):
        self.currency_id = currency_id
        self.code = code
        self.name = name


# =========================
# TRANSACTION CLASS
# =========================

class Transaction:

    def __init__(
        self,
        transaction_id,
        customer,
        amount,
        exchange_rate,
        from_currency,
        to_currency
    ):
        self.transaction_id = transaction_id
        self.customer = customer
        self.amount = amount
        self.exchange_rate = exchange_rate
        self.from_currency = from_currency
        self.to_currency = to_currency

        # Calculate converted amount
        self.total_amount = amount * exchange_rate

        self.status = "Completed"

    def display_transaction(self):

        print("\n===== MONEY EXCHANGE TRANSACTION =====")
        print("Transaction ID:", self.transaction_id)
        print("Customer:", self.customer.full_name)
        print("From Currency:", self.from_currency)
        print("To Currency:", self.to_currency)
        print("Amount:", self.amount)
        print("Exchange Rate:", self.exchange_rate)
        print("Total Amount:", self.total_amount)
        print("Status:", self.status)


# =========================
# MAIN PROGRAM
# =========================

def main():

    # =========================
    # CREATE DATABASE
    # =========================

    create_database()

    # =========================
    # CUSTOMER INFORMATION
    # =========================

    print("\n===== CUSTOMER INFORMATION =====")

    customer_name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    address = input("Enter customer address: ")

    # Save customer to database
    customer_id = save_customer(
        customer_name,
        email,
        phone,
        address
    )

    # Create Customer object
    customer = Customer(
        customer_id,
        customer_name,
        email,
        phone,
        address
    )

    # =========================
    # CURRENCY SELECTION
    # =========================

    print("\n===== SELECT CURRENCY =====")
    print("1. USD - US Dollar")
    print("2. NZD - New Zealand Dollar")
    print("3. PHP - Philippine Peso")
    print("4. AUD - Australian Dollar")

    currency_options = {
        "1": "USD",
        "2": "NZD",
        "3": "PHP",
        "4": "AUD"
    }

    from_choice = input(
        "Choose the currency you have (1-4): "
    )

    to_choice = input(
        "Choose the currency you want (1-4): "
    )

    from_currency = currency_options.get(from_choice)
    to_currency = currency_options.get(to_choice)

    # =========================
    # VALIDATE CURRENCY
    # =========================

    if from_currency is None or to_currency is None:
        print("Invalid currency selection.")
        return

    if from_currency == to_currency:
        print("The currencies cannot be the same.")
        return

    # =========================
    # AMOUNT
    # =========================

    try:

        amount = float(
            input(f"Enter amount in {from_currency}: ")
        )

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:

        print("Please enter a valid number.")
        return

    # =========================
    # EXCHANGE RATE
    # =========================

    try:

        exchange_rate = float(
            input(
                f"Enter exchange rate "
                f"({from_currency} to {to_currency}): "
            )
        )

        if exchange_rate <= 0:
            print("Exchange rate must be greater than 0.")
            return

    except ValueError:

        print("Please enter a valid number.")
        return

    # =========================
    # CREATE TRANSACTION
    # =========================

    transaction = Transaction(
        transaction_id=0,
        customer=customer,
        amount=amount,
        exchange_rate=exchange_rate,
        from_currency=from_currency,
        to_currency=to_currency
    )

    # =========================
    # SAVE TRANSACTION
    # =========================

    transaction_id = save_transaction(
        customer.customer_id,
        transaction.from_currency,
        transaction.to_currency,
        transaction.amount,
        transaction.exchange_rate,
        transaction.total_amount,
        transaction.status
    )

    # Update transaction ID
    transaction.transaction_id = transaction_id

    # =========================
    # DISPLAY RESULT
    # =========================

    transaction.display_transaction()


# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":
    main()