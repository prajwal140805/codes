# Recipe database
recipes = {
    "Pasta": {
        "serving_size": 1,  
        "ingredients": {
            "Pasta (g)": 100,
            "Tomato Sauce (ml)": 150,
            "Cheese (g)": 50,
            "Salt (g)": 10
        }
    },
    "Omelette": {
        "serving_size": 1,
        "ingredients": {
            "Eggs": 2,
            "Salt (g)": 5,
            "Butter (g)": 10
        }
    }
}

print(" Available Dishes:")
for i, dish in enumerate(recipes, 1):
    print(f"{i}. {dish}")

choice = int(input("\nSelect a dish by number: "))
dish_name = list(recipes.keys())[choice - 1]

quantity = int(input(f"How many servings of {dish_name} do you want to make? "))

recipe = recipes[dish_name]
print(f"\n Ingredients for {quantity} serving(s) of {dish_name}:\n")

for item, base_qty in recipe["ingredients"].items():
    total_qty = base_qty * quantity
    print(f"{item}: {total_qty}")
