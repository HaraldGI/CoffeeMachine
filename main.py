from menu import MENU
from menu import resources


change_back = 0
money_earned = 0
turnoff = True


def amount_of_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters: ")) * 0.25
    dimes = int(input("how many dimes: ")) * 0.10
    nickles = int(input("how many nickles: ")) * 0.05
    pennies = int(input("how many pennies: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)


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
    your_money = amount_of_money()
    if your_money >= MENU[coffee_choice]['cost']:
        current_change = your_money - MENU[coffee_choice]['cost']
        # money_earned = money_earned + MENU[coffee_choice]['cost']
        return current_change,  # money_earned
    # Need a way to return money_earned from the buy. So it can be used in the rapport.
    else:
        print(f"You don't have enough money, here is {your_money}$ back.")
        # TODO: 7. Add a way to deduct from resources after the amount of money needed is checked.

def money_summary(choice):
    return MENU[choice]['cost'] + money_earned

while turnoff:
    choice = input("What would you like? espresso/latte/cappuccino")
    if choice == "off":
        turnoff = False
    elif choice == "report":
        print(f"""The current values are:
    Water: {resources['water']}
    Milk: {resources['milk']}
    Coffee: {resources['coffee']}
    Money: {money_earned}$""")
    elif choice == "latte":
        machine_change = check_resources('latte')
        change_back = machine_change
        money_earned = money_summary(choice)
    elif choice == "espresso":
        machine_change = check_resources('espresso')
        change_back = machine_change
        money_earned = money_summary(choice)
    elif choice == "cappuccino":
        machine_change = check_resources('cappuccino')
        change_back = machine_change
        print(f"You get {change_back}$ back.")
        money_earned = money_summary(choice)
    else:
        print("Please make a valid choice.")




# TODO: 1.1 Check if there is enough resources for the different coffee types.

# TODO: 2. When asked to report, pull out info from resources.

# TODO: 3. Ask how many of each coin the user has. Quarters = 0.25, Dimes = 0.10, Nickles = 0.05 and Pennies = 0.01

# TODO: 4. Check if transaction is sufficient. If there is enough money and/or enough resources.

# TODO: 5. If successfull and enough resources and money. Make coffee and deduct from resources and give back change.
