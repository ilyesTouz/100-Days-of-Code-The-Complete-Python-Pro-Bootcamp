from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
cm = CoffeeMaker()
money_machine = MoneyMachine()
money = 0

while True:
    # Choice coffee
    print('What would you like ?')
    for x,y in enumerate(m.menu):
        print(x, y.name)

    # User input
    choice = input('Choice : ')
    
    # Turn off the machine
    if choice=='off':
        print('You turn off the machine')
        break
    
    # Show report
    elif choice=='report' :
        print("""
    ###REPORT###
        """)
        cm.report()
        print('Money : ${}'.format(money))
        break
    
    # Coffee selected
    else:     
        print('You have selected the {}'.format(m.menu[int(choice)].name))
        
        # The resources are sufficient
        if cm.is_resource_sufficient(m.menu[int(choice)]):
            
            # Process coins and Make payment
            transaction = money_machine.make_payment(m.menu[int(choice)].cost)

            # Check if transaction successful
            if transaction:
                
                # Make a coffee
                cm.make_coffee(m.menu[int(choice)])
                
                # Report
                cm.report()
                money_machine.report()

        # The resources aren't sufficient
        else:
            cm.is_resource_sufficient(m.menu[int(choice)])




        



    
    

