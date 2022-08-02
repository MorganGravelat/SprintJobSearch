MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
"cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.0
measure = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}

commands = ["off", "report"]
machine_running = True
def checkmachine(beverage):
    rescost = beverage['ingredients']
    drink = {'water': rescost['water'], 'milk': rescost['milk'],
             'coffee': rescost['coffee']}
    cost = beverage['cost']
    for resource in resources:
        lvl = resources[resource]
        using = drink[resource]
        if lvl - using < 0:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True

def coin_machine():
    total = 0
    if can_buy:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 25
        dimes = int(input("How many dimes?: ")) * 10
        nickels = int(input("How many nickels?: ")) * 5
        pennies = int(input("How many pennies?: "))
        total = float((quarters + dimes + nickels + pennies) / 100)
    print(total)
    return total

def adjust_resource(resources, bev):
    new_resources = resources
    new_resources['water'] = new_resources['water'] - bev['water'] if bev['water'] else new_resources['water']
    new_resources['milk'] = new_resources['milk'] - bev['milk'] if bev['milk'] else new_resources['milk']
    new_resources['coffee'] = new_resources['coffee'] - bev['coffee'] if bev['coffee'] else new_resources['coffee']
    return new_resources

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
while machine_running:
    beverage = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while beverage not in MENU and beverage not in commands:
        beverage = input("Please pick a beverage from these options! (espresso/latte/cappuccino): ").lower()
    bvrginfo = MENU[beverage]
    if beverage == 'off':
        machine_running = False
        print('\n🤖 Powering Down 🤖')
        continue
    elif beverage == 'report':
        for resource in resources:
            print(f"{resource}: {resources[resource]}{measure[resource]}")
        print(f"money: ${money}")
        continue
    elif beverage == 'refill':
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    can_buy = checkmachine(bvrginfo)
    if not can_buy:
        continue
    total = coin_machine()
    if bvrginfo['cost'] > total:
        print("Sorry that's not enough money. Money refunded.")
        continue
    print(resources)
    resources = adjust_resource(resources, bvrginfo['ingredients'])
    print(resources)
