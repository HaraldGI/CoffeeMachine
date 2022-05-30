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
    return MENU[chosen_choice]['cost'] + money_earned


while turnoff:
    choice = input("What would you like? espresso/latte/cappuccino: ")
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
        print(f"Here is your change: {machine_change}$")
        if machine_change != 0:
            money_earned = money_summary(choice)
    elif choice == "espresso":
        machine_change = check_resources('espresso')
        print(f"Here is your change: {machine_change}$")
        if machine_change != 0:
            money_earned = money_summary(choice)
    elif choice == "cappuccino":
        machine_change = check_resources('cappuccino')
        print(f"Here is your change: {machine_change}$")
        if machine_change != 0:
            money_earned = money_summary(choice)
    else:
        print("Please make a valid choice.")
