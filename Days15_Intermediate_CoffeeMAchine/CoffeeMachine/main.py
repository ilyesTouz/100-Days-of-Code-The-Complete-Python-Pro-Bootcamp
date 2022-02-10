
### Variables ###
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


### TODO LIST ####

# TODO 1 : Prompt user by asking "What you would like ?" (espresso/latte/cappuncino)
def choice_coffee():
    try:
        choice = int(input("""What you would like ? 
         1 : Espresso
         2 : Latte
         3 : Cappucino 
         Choice : """
        ))
        print('You have selected {}'.format(list(MENU.keys())[choice-1]))
        return list(MENU.keys())[choice-1]
    except choice == 'off':
           print('You turn off the machine') 
    except ValueError: 
        print("Your choice is not a integer, or it's not between 1 and 3")

# TODO 2 : Turn off the machine
def off(cmd):
    if cmd == 'off':
        print('You turn off the machine')

# TODO 3 : Print report
def report_resources(resources):
    metrics = ['ml', 'ml', 'g']
    for key, met in zip(resources.keys(), metrics):
        print('{}: {} {}'.format(key, resources[key], met))

# TODO 4 : Check if the resources sufficient
def check_resources_sufficient(MENU, choice_coffee, resources):
    need_resources = MENU[choice_coffee]["ingredients"]
    
    for ingredient in need_resources.keys():
        if need_resources[ingredient] > resources[ingredient]:
            print('​Sorry there is not enough {}'.format(ingredient))
        else:
            print('​There is enough {}'.format(ingredient))

# TODO 5 : Process Coin
def insert_coins(MENU, choice):
    coffee_cost = MENU[choice]["cost"]
    money_conversion = {'quarters' : 0.25, 'dimes' : 0.10, 
        'nickles': 0.05, 'pennies' : 0.01}
    coins_inserted = 0

    for money in money_conversion.keys():
        coins_insert = float(input("""How many {} coins want you insert ? """.format(money)))
        coins_inserted += money_conversion[money]*coins_insert
        print('Money inserted : {} $'.format(coins_inserted))
    
    print('You have inserted {} $'.format(coins_inserted))
    return coins_inserted

# TODO 6 : 
def check_transactions(coins_inserted, choice):
    coffee_cost = MENU[choice]["cost"]
    profit = 0

    if coins_inserted < coffee_cost:
        print("​Sorry that's not enough money. Money refunded​")
        return False
        
    elif coins_inserted > coffee_cost:
        print("Here is {} dollars in change.".format(float(coins_inserted-coffee_cost)))
        profit += coffee_cost
        print('Transaction successfull')
        return True, profit

    else:
        profit += coffee_cost
        print('Transaction successfull')
        return True, profit

# TODO 7 Make a Coffee : 
def make_coffee(MENU, choice, resources):
    report_resources(resources)


# MAIN
while True:
    choice = choice_coffee()
    check_resources_sufficient(MENU, choice, resources)
    coins = insert_coins(MENU, choice)
    check_transactions(coins, choice)