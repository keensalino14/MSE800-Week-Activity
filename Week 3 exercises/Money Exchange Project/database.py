import sqlite3
import os


DATABASE_NAME = os.path.join(
    os.path.dirname(__file__),
    "Money Exchange Project.db"
)


# =========================
# CREATE DATABASE
# =========================

def create_database():

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Customer table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL
        )
    """)

    # Currency table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currency (
            currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            name TEXT NOT NULL
        )
    """)

    # Transaction table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaction_table (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            from_currency TEXT NOT NULL,
            to_currency TEXT NOT NULL,
            amount REAL NOT NULL,
            exchange_rate REAL NOT NULL,
            total_amount REAL NOT NULL,
            status TEXT NOT NULL,

            FOREIGN KEY (customer_id)
                REFERENCES customer(customer_id)
        )
    """)

    connection.commit()
    connection.close()


# =========================
# SAVE CUSTOMER
# =========================

def save_customer(full_name, email, phone, address):

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Customer (
            full_name,
            email,
            phone,
            address
        )
        VALUES (?, ?, ?, ?)
    """, (
        full_name,
        email,
        phone,
        address
    ))

    customer_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return customer_id


# =========================
# SAVE TRANSACTION
# =========================

def save_transaction(
    customer_id,
    from_currency,
    to_currency,
    amount,
    exchange_rate,
    total_amount,
    status
):

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO transaction_table (
            customer_id,
            from_currency,
            to_currency,
            amount,
            exchange_rate,
            total_amount,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        customer_id,
        from_currency,
        to_currency,
        amount,
        exchange_rate,
        total_amount,
        status
    ))

    transaction_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return transaction_id