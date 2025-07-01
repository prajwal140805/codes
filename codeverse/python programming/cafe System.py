import msvcrt
import os
from cafe_menu import menu

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
