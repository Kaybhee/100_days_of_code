from main import MENU, resources
# # print(MENU)
profit = 0
def resource_sufficient(drink_type):
    for items in resources and drink_type:
        if drink_type[items] >= resources[items]:
            print(f"sorry there's not enough {items}")
            return False
        else:
            return True


def payment():
    print("please insert coins")
    amount = int(input("How many quarters?: ")) * 0.25
    amount += int(input("How many dimes?: ")) * 0.10
    amount += int(input("How many nickles?: ")) * 0.05
    amount += int(input("How many pennies?: ")) * 0.01
    return amount


def make_coffee(drink_type, drink_ingredients):
    for item in drink_ingredients and resources:
        resources[item] -= drink_ingredients[item]
        print(f"Here is your {drink_type}")


def is_transfer_successful(payment_processed, drink_cost):
    if payment_processed >= drink_cost:
        change = round(payment_processed - drink_cost, 2)
        print(f"Here is the ${change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False

do_continue = False

while not do_continue:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "off":
        do_continue = True
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml")  
        print(f"Milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: {profit}")
    elif coffee_type == "":
        do_continue = True
    else:
        drink = MENU[coffee_type]
        if resource_sufficient(drink["ingredients"]):
            output_pay = payment() 
            if is_transfer_successful(output_pay,  drink["cost"]):
                make_coffee(coffee_type, drink["ingredients"])


# for item in resources:
#     drink_resources = resources[item]

    
# def drink()
# coffee_espresso = MENU["espresso"]
# coffee_latte = MENU["latte"]
# coffee_cappuccino = MENU["cappuccino"]

# order_type = input("What would you like to order? (espresso/latte/cappuccino): ")
# if order_type == "latte":
#         print("Please insert coins. \n")
#         coin_
#         result = int(0.25 * coin_quarters + 0.1 * coin_dime + 0.05 * coin_nickles + 0.01 * coin_pennies)
#         compare = (MENU["latte"]["cost"])
#         if result > compare:
#             print(f" Here is ${result - compare} in change ")


