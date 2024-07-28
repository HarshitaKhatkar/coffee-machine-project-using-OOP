from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
money_machine = MoneyMachine()
item_report = CoffeeMaker()
items = Menu()

while machine_on:
    user_choice = input(f"what would you like? {items.get_items()} ").lower()

    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        item_report.report()
        money_machine.report()
    else:
        drink = items.find_drink(user_choice)
        sufficient = item_report.is_resource_sufficient(drink)
        if sufficient and money_machine.make_payment(drink.cost):
            item_report.make_coffee(drink)





