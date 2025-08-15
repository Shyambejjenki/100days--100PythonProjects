# Shopping Cart

# Step 1: Predefined store items as tuples (name, price)
store_items = [
    ("tomato", 20),
    ("Banana", 5),
    ("curd", 15),
    ("Milk", 20),
    ("sugar", 25)
]

# Step 2: Empty cart (list)
cart = []

# Step 3: Menu loop
while True:
    print("\n--- Welcome to the Store ---")
    print("1. View Store Items")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Remove Item from Cart")
    print("5. Checkout & Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nAvailable Items:")
        for index, item in enumerate(store_items, start=1):
            print(f"{index}. {item[0]} - ₹{item[1]}")

    elif choice == "2":
        item_no = int(input("Enter item number to add: "))
        if 1 <= item_no <= len(store_items):
            cart.append(store_items[item_no - 1])
            print(f"{store_items[item_no - 1][0]} added to cart!")
        else:
            print("Invalid item number!")

    elif choice == "3":
        if cart:
            print("\nItems in your cart:")
            total = 0
            for item in cart:
                print(f"- {item[0]} - ₹{item[1]}")
                total += item[1]
            print(f"Total: ₹{total}")
        else:
            print("Your cart is empty!")

    elif choice == "4":
        if cart:
            print("\nCart Items:")
            for index, item in enumerate(cart, start=1):
                print(f"{index}. {item[0]} - ₹{item[1]}")
            remove_no = int(input("Enter item number to remove: "))
            if 1 <= remove_no <= len(cart):
                removed_item = cart.pop(remove_no - 1)
                print(f"{removed_item[0]} removed from cart!")
            else:
                print("Invalid number!")
        else:
            print("Your cart is empty!")

    elif choice == "5":
        if cart:
            total = sum(price for _, price in cart)
            print("\nThank you for shopping!")
            print(f"Your total bill is ₹{total}")
        else:
            print("Thank you! Your cart was empty.")
        break

    else:
        print("Invalid choice! Please select 1-5.")
