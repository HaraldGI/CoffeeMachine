from menu import MENU
from menu import resources


change_back = 0
money_earned = 0
turnoff = True
boughtcoffee = True


def amount_of_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters: ")) * 0.25
    dimes = int(input("how many dimes: ")) * 0.10
    nickles = int(input("how many nickles: ")) * 0.05
    pennies = int(input("how many pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_resources(coffee_choice):
    # Checks if there is enough resources
    if MENU[coffee_choice]['ingredients']['water'] <= resources['water']:
        new_water = resources['water'] - MENU[coffee_choice]['ingredients']['water']
        resources['water'] = new_water
        if MENU[coffee_choice]['ingredients']['milk'] <= resources['milk']:
            new_milk = resources['milk'] - MENU[coffee_choice]['ingredients']['milk']
            resources['milk'] = new_milk
            if MENU[coffee_choice]['ingredients']['coffee'] <= resources['coffee']:
                new_coffee = resources['coffee'] - MENU[coffee_choice]['ingredients']['coffee']
                resources['coffee'] = new_coffee
                your_money = amount_of_money()
                # Checks if there is enough money.
                if your_money >= MENU[coffee_choice]['cost']:
                    current_change = your_money - MENU[coffee_choice]['cost']
                    print(f"Here is your {coffee_choice}, enjoy!")
                    return round(current_change, 2)
                else:
                    print(f"You don't have enough money, here is {your_money}$ back.")
                    current_change = 0
                    return current_change
            else:
                current_change = 0
                print("Not enough coffee")
                return current_change
        else:
            current_change = 0
            print("Not enough milk.")
            return current_change
    else:
        current_change = 0
        print("Not enough water.")
        return current_change


def money_summary(chosen_choice):
    # Adds money from buyer to money earned.
    return MENU[chosen_choice]['cost'] + money_earned


def change(coffee_type):
    # Checks if there is any change for the buyer. Print a different message if there is no change.
    global money_earned
    machine_change = check_resources(coffee_type)
    if machine_change > 0:
        print(f"Here is your change: {machine_change}$")
    if machine_change != 0:
        money_earned = money_summary(choice)


while turnoff:
    # Main loop.
    choice = input("What would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        print("Turns off the coffee machine. Please wait.")
        turnoff = False
    elif choice == "report":
        print(f"""The current values are:
    Water: {resources['water']}
    Milk: {resources['milk']}
    Coffee: {resources['coffee']}
    Money: {money_earned}$""")
    # Refills the Water, Milk and Coffee.
    elif choice == "refill":
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    elif choice == 'latte':
        change('latte')
    elif choice == 'espresso':
        change('espresso')
    elif choice == 'cappuccino':
        change('cappuccino')
    else:
        print("Please make a valid choice.")
