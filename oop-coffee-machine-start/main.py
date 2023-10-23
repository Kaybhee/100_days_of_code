from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print(MenuItem)
# Print report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# check if resources is sufficient
want_continue = False
menu = Menu()

while not want_continue:
    choice = menu.get_items()
    drink_choice = input(f"What would you like? {choice}: ")
    if drink_choice == "off":
        want_continue = True
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink_choice)
        #print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
