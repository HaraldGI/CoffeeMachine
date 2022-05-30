from menu import MENU
from menu import resources

# TODO: 6. Make while loop that turns the machine off.

# TODO: 1. Prompt user what they would like: espresso/latte/cappuccino

your_money = 0
machine_change = 0


def check_resources(coffee_choice):
    if MENU[coffee_choice]['ingredients']['water'] <= resources['water']:
        new_water = resources['water'] - MENU[coffee_choice]['ingredients']['water']
        resources['water'] = new_water
    else:
        print("Not enough water.")
        if MENU[coffee_choice]['ingredients']['milk'] <= resources['milk']:
            new_milk = resources['milk'] - MENU[coffee_choice]['ingredients']['milk']
            resources['milk'] = new_milk
        else:
            print("Not enough milk.")
            if MENU[coffee_choice]['ingredients']['coffee'] <= resources['coffee']:
                new_coffee = resources['coffee'] - MENU[coffee_choice]['ingredients']['coffee']
                resources['coffee'] = new_coffee
            else:
                print("Not enough coffee")
                if your_money >= MENU[coffee_choice]['cost']:
                    machine_change = your_money - MENU[coffee_choice]['cost']
                    return machine_change
                # TODO: 7. Add a way to return the change.


choice = input("What would you like? espresso/latte/cappuccino")

if choice == "report":
    print(f"""The current values are:
Water: {resources['water']}
Milk: {resources['milk']}
Coffee: {resources['coffee']}
Change: {money}$""")
elif choice == "latte":
    check_resources('latte')

# TODO: 1.1 Check if there is enough resources for the different coffee types.

# TODO: 2. When asked to report, pull out info from resources.

# TODO: 3. Ask how many of each coin the user has. Quarters = 0.25, Dimes = 0.10, Nickles = 0.05 and Pennies = 0.01

# TODO: 4. Check if transaction is sufficient. If there is enough money and/or enough resources.

# TODO: 5. If successfull and enough resources and money. Make coffee and deduct from resources and give back change.
