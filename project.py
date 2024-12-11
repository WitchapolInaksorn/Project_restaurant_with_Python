import random

# Main Menu
def mainmenu():
    print("\n================== [MAIN MENU] ==================")
    print("1. Food Order")
    print("2. Drink Order")
    print("3. Random Food")
    print("4. Random Drink")
    print("0. Exit Program")
    print("=================================================")

# Menu 1: Food Order
def menu_food():
    while True:
        print("\n[Food Order]")
        if work == 0:
            return 0
        elif work == 1:
            list_food()
        else:
            pass

# Menu 2: Drink Order
def menu_drink():
    while True:
        print("\n[Drink Order]")
        if work == 0:
            return 0
        elif work == 2:
            list_drink()
        else:
            pass

# Menu 3: Random Food
def menu_foodrand():
    while True:
        print("\n[Random Food]")
        if work == 0:
            return 0
        elif work == 3:
            rand_food()
        else:
            pass

# Menu 4: Random Drink
def menu_drinkrand():
    while True:
        print("\n[Random Drink]")
        if work == 0:
            return 0
        elif work == 4:
            rand_drink()
        else:
            pass

# Function 1: List Food
def list_food():
    print("\n================ [FOOD MENU] ================")
    print("<< Single Dishes >>")
    print("1: Mixed Fried Rice - 50 THB")
    print("2: Fried Rice with Crispy Pork and Kale - 50 THB")
    print("3: Basil Pork Fried Rice - 40 THB")
    print("4: Garlic Pork Fried Rice - 40 THB")
    print("<< Stir-fried/Deep-fried Dishes >>")
    print("5: Shrimp Cakes - 55 THB")
    print("6: Fried Shrimp - 55 THB")
    print("7: Stir-fried Curry Powder - 65 THB")
    print("8: Stir-fried Spicy Seafood - 65 THB")
    print("<< Soups >>")
    print("9: Clear Soup with Minced Pork - 50 THB")
    print("10: Hot & Spicy Soup (Tom Klong) - 50 THB")
    print("11: Chicken Feet Super Soup - 60 THB")
    print("12: Seafood Tom Yum Soup - 60 THB")
    print("0: Confirm Your Order")
    print("============================================")

    sum_food = 0
    item = 1
    while item > 0:
        item = int(input("Choose a menu item: "))
        if item == 1 or item == 2:
            sum_food += 50
        elif item == 3 or item == 4:
            sum_food += 40
        elif item == 5 or item == 6:
            sum_food += 55
        elif item == 7 or item == 8:
            sum_food += 65
        elif item == 9 or item == 10:
            sum_food += 50
        elif item == 11 or item == 12:
            sum_food += 60
        elif item == 0:
            break
        else:
            print("The menu item you selected is not available.")
    print("Total price:", sum_food, "THB")
    while sum_food != 0:
        print("\n<<Payment Menu>>")
        cash = int(input("Cash: "))
        if cash < sum_food:
            print("Insufficient funds. Please try again.")
        elif cash >= sum_food:
            change = cash - sum_food
            break
    print("Change:", change, "THB")

# Function 2: List Drinks
def list_drink():
    print("\n================ [DRINK MENU] ================")
    print("<< Hot Drinks >>")
    print("1: Americano - 30 THB")
    print("2: Espresso - 30 THB")
    print("3: Mocha - 30 THB")
    print("4: Latte - 30 THB")
    print("<< Iced Drinks >>")
    print("5: Thai Iced Tea - 30 THB")
    print("6: Green Tea - 30 THB")
    print("7: Fresh Milk - 30 THB")
    print("8: Ovaltine - 30 THB")
    print("<< Blended Drinks >>")
    print("9: Ovaltine Bear - 35 THB")
    print("10: Strawberry Bear - 35 THB")
    print("11: Honey Bear - 40 THB")
    print("12: Brown Sugar Bear - 40 THB")
    print("0: Confirm Your Order")
    print("============================================")
    
    sum_food = 0
    item = 1
    while item > 0:
        item = int(input("Choose a menu item: "))
        if item == 1 or item == 2 or item == 3 or item == 4:
            sum_food += 30
        elif item == 5 or item == 6 or item == 7 or item == 8:
            sum_food += 30
        elif item == 9 or item == 10:
            sum_food += 35
        elif item == 11 or item == 12:
            sum_food += 40
        elif item == 0:
            break
        else:
            print("The drink you selected is not available.")
    print("Total price:", sum_food, "THB")
    while sum_food != 0:
        print("\n<<Payment Menu>>")
        cash = int(input("Cash: "))
        if cash < sum_food:
            print("Insufficient funds. Please try again.")
        elif cash >= sum_food:
            change = cash - sum_food
            break
    print("Change:", change, "THB")

# Function 3: Random Food
def rand_food():
    print("\n[Random Food]")
    randfood = ["Stir-fried Basil with Minced Pork", "Fried Rice with Mixed Meat", "Fried Rice with Crispy Pork and Kale", "Fried Rice with Curry", "Minced Pork Omelette with Rice", "Garlic Pork on Rice", "Stir-fried Instant Noodles", "Seafood Sukiyaki", "Tom Yum Seafood", "Stir-fried Noodles with Soy Sauce", "Crispy Seafood in Gravy", "Tofu Soup with Minced Pork", "Pad Thai with Seafood"]
    guess = random.randint(0, len(randfood) - 1)
    print(f'Congratulations! You got: {randfood[guess]}')

# Function 4: Random Drink
def rand_drink():
    print("\n[Random Drink]")
    randdrink = ["Thai Tea", "Green Tea", "Cocoa", "Iced Coffee", "Strawberry Yogurt", "Iced Ovaltine", "Milk", "Lemon Tea", "Iced Black Coffee", "Iced Chocolate", "Red Lime Soda", "Blue Hawaii"]
    guess = random.randint(0, len(randdrink) - 1)
    print(f'Congratulations! You got: {randdrink[guess]}')

# Greeting
def meet(name):
    print(f'<<Food4U>>\nWelcome, {name}!')
    print()

# Farewell
def farewell(name):
    print()
    print(f"Thank you, {name}, for visiting us.")
    print("----- Food4U -----")

# Input Customer Name
name = input("Customer Name: ")
meet(name)

# Main Loop
while True:
    mainmenu()
    work = int(input("Please select an option from the menu above: "))
    print("------------------------------------------------")
    if work == 0:
        farewell(name)
        break
    elif work == 1:
        if list_food() == 0:
            farewell(name)
            break
    elif work == 2:
        if list_drink() == 0:
            farewell(name)
            break
    elif work == 3:
        if rand_food() == 0:
            farewell(name)
            break
    elif work == 4:
        if rand_drink() == 0:
            farewell(name)
            break
    else:
        pass
