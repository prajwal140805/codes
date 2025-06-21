from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Important for session security

menu = {
    'Starters': {
        'Panner Chilli': 120,
        'Pav Bhaji': 90,
        'Gobi Manchurian': 100,
        'Mushroom Manchurian': 110,
        'Chicken Chilli': 130
    },
    'Main Course': {
        'North Indian Thali': 180,
        'South Indian Thali': 160,
        'Non Veg Thali': 200,
        'Kaju Masala': 150,
        'Veg Curry': 130,
        'Paneer Masala': 140,
        'Mixed Veg Curry': 130,
        'Butter Naan': 30,
        'Garlic Naan': 40
    },
    'Rice': {
        'Chicken Biryani': 150,
        'Hyderabadi Chicken Biryani': 170,
        'Ghee Rice': 100,
        'Jeera Rice': 80,
        'Paneer Rice': 120
    },
    'South Indian': {
        'Idli Vada': 60,
        'Masala Dosa': 70,
        'Puri': 60,
        'Set Dosa': 65,
        'Uttapam': 70
    },
    'Fast Food': {
        'Samosa': 20,
        'Pani Puri': 30,
        'Veg Burger': 70,
        'Chicken Burger': 90,
        'French Fries': 60
    },
    'Desserts': {
        'Pastry': 50,
        'Ice Cream': 60,
        'Apple Pie': 70,
        'Almond Malai Kulfi': 80,
        'Chocolate Brownies': 90
    },
    'Beverages': {
        'Coffee': 30,
        'Chai': 20,
        'Coke': 40,
        'Lassi': 50,
        'Mango Shake': 60
    },
    'Cold Drinks': {
        'Sprite': 45,
        'Mirinda': 45,
        'Coke': 45,
        'Sting': 20,
        'Pepsi': 45
    }
}


@app.route('/', methods=['GET', 'POST'])
def cafe():
    # Initialize session orders if not exists
    if 'orders' not in session:
        session['orders'] = []

    selected_category = None
    bill = None
    total_amt = 0

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            selected_category = request.form.get('category')
            item = request.form.get('item')
            quantity = request.form.get('quantity')

            if selected_category and item and quantity:
                try:
                    quantity = int(quantity)
                    if quantity > 0:
                        # Get price from menu
                        price = menu[selected_category][item]
                        total = price * quantity

                        # Add to session orders
                        session['orders'] = session.get('orders', []) + [{
                            'category': selected_category,
                            'item': item,
                            'qty': quantity,
                            'total': total
                        }]
                        session.modified = True
                except (ValueError, KeyError):
                    # Handle invalid quantity or missing menu item
                    pass

        elif action == 'bill':
            # Generate bill from session orders
            bill = session.get('orders', [])
            total_amt = sum(order['total'] for order in bill)
            # Clear session orders
            session['orders'] = []

        elif action == 'clear':
            # Clear current orders
            session['orders'] = []

    return render_template(
        'cafe.html',
        menu=menu,
        orders=session.get('orders', []),
        bill=bill,
        total_amt=total_amt,
        selected_category=selected_category
    )


if __name__ == '__main__':
    app.run(debug=True)
