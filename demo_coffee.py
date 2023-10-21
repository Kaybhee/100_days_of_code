from main import MENU, resources
want_continue = False
profit = 0


def is_resource_sufficient(drink_ingredient):
    """To check if the resources are sufficient and compare between the drink and resources"""
    for items in resources:
        if drink_ingredient[items] >= resources[items]:
            print(f"Sorry there's not enough {items}")
            return False
        else:
            return True


def process_coins():
    """This takes the user coins and calculates the monetary value"""
    print("Please insert some coins")
    amount_inserted = int(input("How many quarters: ")) * 0.25
    amount_inserted += int(input("How many nickles: ")) * 0.10
    amount_inserted += int(input("How many pennies: ")) * 0.05
    amount_inserted += int(input("How many pennies: ")) * 0.01
    return amount_inserted


def is_transaction_successful(ingredient_cost, payment):
    """To check the money input and compare with the drink cost"""
    if payment >= ingredient_cost:
        change = round(payment - ingredient_cost, 2)
        print(f"Here is ${change} dollars in change")
        global profit
        profit += drink["cost"]
        #print(profit)
        # print(report)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """decrement the resources for different types of drink selected and print the drink"""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
        print(f"Here is your {drink_name}. Enjoy!")


while not want_continue:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == "off":
        want_continue = True
    elif coffee_choice == "":
        exit()
    elif coffee_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee_choice]
        is_resource_sufficient(drink["ingredients"])
        payment = process_coins()
        is_transaction_successful(drink["cost"], payment)
        make_coffee(coffee_choice, drink["ingredients"])
      