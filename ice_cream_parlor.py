import sqlite3
import sys

DB_NAME = 'ice_cream_parlor.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
    except sqlite3.Error as e:
        print(e)
    return conn
def view_flavors():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT flavor_name, description, available FROM seasonal_flavors")
        rows = cursor.fetchall()
        print("Seasonal Flavors:")
        for row in rows:
            status = "Available" if row[2] else "Not Available"
            print(f"- {row[0]}: {row[1]} ({status})")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

def view_cart():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT product_name FROM cart")
        rows = cursor.fetchall()
        print("Cart items:")
        for row in rows:
            print(f"- {row[0]}")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

def add_to_cart(product_name):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cart (product_name) VALUES (?)", (product_name,))
        conn.commit()
        print(f"{product_name} added to cart.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

def search_flavors(query):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT flavor_name, description FROM seasonal_flavors WHERE flavor_name LIKE ?", (f'%{query}%',))
        rows = cursor.fetchall()
        print("Search results:")
        for row in rows:
            print(f"- {row[0]}: {row[1]}")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

def add_allergen(allergen_name):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO allergens (allergen_name) VALUES (?)", (allergen_name,))
        conn.commit()
        print(f"Allergen {allergen_name} added.")
    except sqlite3.IntegrityError:
        print(f"Allergen {allergen_name} already exists.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

def view_allergens():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT allergen_name FROM allergens")
        rows = cursor.fetchall()
        print("Allergens:")
        for row in rows:
            print(f"- {row[0]}")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

def main_menu():
    print("\nIce Cream Parlor Menu:")
    print("1. View Seasonal Flavors")
    print("2. View Cart")
    print("3. Add Item to Cart")
    print("4. Search Flavors")
    print("5. Add Allergen")
    print("6. View Allergens")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        view_flavors()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        product_name = input("Enter the product name to add to cart: ")
        add_to_cart(product_name)
    elif choice == '4':
        query = input("Enter the flavor name to search: ")
        search_flavors(query)
    elif choice == '5':
        allergen_name = input("Enter the allergen name to add: ")
        add_allergen(allergen_name)
    elif choice == '6':
        view_allergens()
    elif choice == '7':
        print("Exiting the application. Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice! Please select a valid option.")

if _name_ == '_main_':
    while True:
        main_menu()
