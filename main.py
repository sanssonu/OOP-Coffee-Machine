from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

should_stop = False
while not should_stop:
    types_of_coffee = menu.get_items()
    coffee = input(f"What would you like? {types_of_coffee}: ")

    if coffee == "off":
        should_stop = True
    elif coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee)
        if drink:
            enough_resources = coffee_maker.is_resource_sufficient(drink)
            if enough_resources:
                payment_successful = money_machine.make_payment(drink.cost)
                if payment_successful:
                    coffee_maker.make_coffee(drink)
