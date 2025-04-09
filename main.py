resources = {
    "water": 1000,  
    "milk": 500,   
    "coffee": 300,  
    "income": 0     
}

menu = {
    "Espresso": {"water": 50, "milk": 0, "coffee": 18, "price": 250},   # Price in PHP
    "Latte": {"water": 200, "milk": 150, "coffee": 24, "price": 500},    # Price in PHP
    "Cappuccino": {"water": 250, "milk": 100, "coffee": 24, "price": 600}  # Price in PHP
}

def display_menu():
    print("""
  ______              ______    ______                    
 /      \            /      \  /      \                   
/$$$$$$  |  ______  /$$$$$$  |/$$$$$$  |______    ______  
$$ |  $$/  /      \ $$ |_ $$/ $$ |_ $$//      \  /      \ 
$$ |      /$$$$$$  |$$   |    $$   |  /$$$$$$  |/$$$$$$  |
$$ |   __ $$ |  $$ |$$$$/     $$$$/   $$    $$ |$$    $$ |
$$ \__/  |$$ \__$$ |$$ |      $$ |    $$$$$$$$/ $$$$$$$$/ 
$$    $$/ $$    $$/ $$ |      $$ |    $$       |$$       |
 $$$$$$/   $$$$$$/  $$/       $$/      $$$$$$$/  $$$$$$$/                                                          
""")
    print("{============================}")
    print("\nAvailable Coffee Options:")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("\n{============================}")

def insert_coin(required_amount):
    total_inserted = 0
    while total_inserted < required_amount:
        try:
            coin = float(input(f"\nInsert coin (Remaining: ₱{required_amount - total_inserted}): ₱"))
            if coin > 0:
                total_inserted += coin
            else:
                print("Invalid amount. Please insert a valid coin.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return total_inserted

def select_coffee():
    while True:
        display_menu()
        try:
            choice = int(input("\nSelect your coffee (1, 2, or 3): "))
            if choice == 1:
                return "Espresso"
            elif choice == 2:
                return "Latte"
            elif choice == 3:
                return "Cappuccino"
            else:
                print("Invalid selection. Please choose a valid option (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def check_resources(coffee_choice):
    coffee = menu[coffee_choice]
    if resources["water"] < coffee["water"]:
        print("Sorry, not enough water.")
        return False
    if resources["milk"] < coffee["milk"]:
        print("Sorry, not enough milk.")
        return False
    if resources["coffee"] < coffee["coffee"]:
        print("Sorry, not enough coffee.")
        return False
    return True

def make_coffee(coffee_choice):
    coffee = menu[coffee_choice]
    resources["water"] -= coffee["water"]
    resources["milk"] -= coffee["milk"]
    resources["coffee"] -= coffee["coffee"]
    resources["income"] += coffee["price"]
    print(f"\nHere is your {coffee_choice}! Enjoy!")

def main():
    while True:
        coffee_choice = select_coffee()
        if check_resources(coffee_choice):
            coffee_price = menu[coffee_choice]["price"]
            print(f"\nThe price for {coffee_choice} is: ₱{coffee_price}")
            total_inserted = insert_coin(coffee_price)
            if total_inserted >= coffee_price:
                make_coffee(coffee_choice)
            else:
                print(f"\nNot enough money inserted. ₱{total_inserted} is less than the required ₱{coffee_price}.")
        else:
            print("Please try again later.")

        continue_choice = input("\nWould you like to make another coffee? (yes/no): ").lower()
        if continue_choice != "yes":
            print(f"\nThank you for using the coffee machine! Total income: ₱{resources['income']}")
            break

if __name__ == "__main__":
    main()
