import msvcrt
import os

menu = {
    '1': {'category': "starters", 'items': {
        '1': {'item': "Panner Chilli", 'price': 120},
        '2': {'item': "Pav Bhaji", 'price': 90},
        '3': {'item': "Gobi Manchurian", 'price': 100},
        '4': {'item': "Mushroom Manchurian", 'price': 110},
        '5': {'item': "Chicken Chilli", 'price': 130},
    }},
    '2': {'category': "main course", 'items': {
        '1': {'item': "North Indian Thali", 'price': 180},
        '2': {'item': "South Indian Thali", 'price': 160},
        '3': {'item': "Non Veg Thali", 'price': 200},
        '4': {'item': "Kaju Masala", 'price': 150},
        '5': {'item': "Veg Curry", 'price': 130},
        '6': {'item': "Paneer Masala", 'price': 140},
        '7': {'item': "Mixed Veg Curry", 'price': 130},
        '8': {'item': "Butter Naan", 'price': 30},
        '9': {'item': "Garlic Naan", 'price': 40},
    }},
    '3': {'category': "rice", 'items': {
        '1': {'item': "Chicken Biryani", 'price': 150},
        '2': {'item': "Hyderabadi Chicken Biryani", 'price': 170},
        '3': {'item': "Ghee Rice", 'price': 100},
        '4': {'item': "Jeera Rice", 'price': 80},
        '5': {'item': "Paneer Rice", 'price': 120},
    }},
    '4': {'category': "south indian", 'items': {
        '1': {'item': "Idli Vada", 'price': 60},
        '2': {'item': "Masala Dosa", 'price': 70},
        '3': {'item': "Puri", 'price': 60},
        '4': {'item': "Set Dosa", 'price': 65},
        '5': {'item': "Uttapam", 'price': 70},
    }},
    '5': {'category': "fast food", 'items': {
        '1': {'item': "Samosa", 'price': 20},
        '2': {'item': "Pani Puri", 'price': 30},
        '3': {'item': "Veg Burger", 'price': 70},
        '4': {'item': "Chicken Burger", 'price': 90},
        '5': {'item': "French Fries", 'price': 60},
    }},
    '6': {'category': "desserts", 'items': {
        '1': {'item': "Pastry", 'price': 50},
        '2': {'item': "Ice Cream", 'price': 60},
        '3': {'item': "Apple Pie", 'price': 70},
        '4': {'item': "Almond Malai Kulfi", 'price': 80},
        '5': {'item': "Chocolate Brownies", 'price': 90},
    }},
    '7': {'category': "beverages", 'items': {
        '1': {'item': "Coffee", 'price': 30},
        '2': {'item': "Chai", 'price': 20},
        '3': {'item': "Coke", 'price': 40},
        '4': {'item': "Lassi", 'price': 50},
        '5': {'item': "Mango Shake", 'price': 60},
    }},
}

orders = []  # Store selected orders

def bill():
    os.system('cls')
    print("\n_____Bill______ ")
    total_amount = 0
    print("-" * 50)
    print(f"{'Item':<20}{'Qty':>5} x {'Price':>5} = {'Total':>6}")
    print("-" * 50)
    for order in orders:
        print(f"{order['item']:<20}{order['qty']:>5} x ₹{order['price']:>5} = ₹{order['total']:>6}")
        total_amount += order['total']
    print("-" * 50)
    print(f"{'_____TOTAL BILL_____':<35}= ₹{total_amount}")
    print("Thank you")
    exit()

def printmenu():
    while True:
        os.system('cls')
        print("\n_____MENU_____\n")
        for category_id, category_data in menu.items():
            print(f"{category_id}. {category_data['category'].upper()}")

        key = msvcrt.getch()
        if key == b'\x1b':  # ESC
            bill()
        if not key.isdigit():
            continue
        category_id = key.decode()
        if category_id not in menu:
            continue

        category_data = menu[category_id]
        os.system('cls')
        print(f"\n{category_data['category'].upper()} MENU:")
        for item_id, item_data in category_data['items'].items():
            print(f"{item_id}. {item_data['item']:<26} - ₹{item_data['price']}")
        item_key = msvcrt.getch()
        if not item_key.isdigit():
            continue
        item_id = item_key.decode()

        if item_id not in category_data['items']:
            continue

        item_data = category_data['items'][item_id]
        os.system('cls')
        print(f"You selected: {item_data['item']} - ₹{item_data['price']}")
        print("Enter quantity:")

        qty_key = msvcrt.getch()
        if not qty_key.isdigit():
            print("Invalid quantity.")
            continue
        qty = int(qty_key.decode())
        total = item_data['price'] * qty
        orders.append({
            'item': item_data['item'],
            'price': item_data['price'],
            'qty': qty,
            'total': total
        })
        print(f"Added {qty} x {item_data['item']} = ₹{total} to order.")
        print("\nPress any key to continue ordering or ESC for bill.")
        next_key = msvcrt.getch()
        if next_key == b'\x1b':
            bill()

printmenu()
