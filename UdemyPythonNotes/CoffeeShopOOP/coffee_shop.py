from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

class CoffeeShop:
    """Models each Part of the Shop"""   # OOP Class creation, instantiation, and initialization
    def __init__(self): # Initialize the Shop with the Menu and the CoffeeMaker and MoneyMachine
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def add_to_menu(self, name, cost, water, milk, coffee):
        item = MenuItem(name, cost, water, milk, coffee)
        self.menu.menu.append(item)
    def make_order(self):
        is_on = True
        while is_on:
            print(self.menu.get_items())
            order = input("Please pick a beverage from these options! ").lower()
            if order == "report":
                self.coffee_maker.report()
                self.money_machine.report()
                continue
            elif order == "off":
                is_on = False
                print('\n🤖 Powering Down 🤖')
                continue
            order = self.menu.find_drink(order)
            if not order:
                continue
            available = self.coffee_maker.is_resource_sufficient(order)
            if not available:
                continue
            payment = self.money_machine.make_payment(order.cost)
            if not payment:
                continue
            self.coffee_maker.make_coffee(order)
