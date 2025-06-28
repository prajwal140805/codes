from flask import Flask, render_template
app = Flask(__name__)

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
    'cold drinks': {
        'sprite': 45,
        'Mirinda': 45,
        'Coke': 45,
        'sting': 20,
        'pepsi': 45
    }
}

@app.route('/')
def index():
    return render_template("index.html", menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
