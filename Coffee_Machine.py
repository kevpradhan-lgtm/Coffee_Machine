from CoffeeMachineData import MENU,resources,logo1,logo2
import os
print(logo1)
print(logo2)
while True:
    Choice=input("What would you like? Espresso/latte/cappuccino):").lower()
    if Choice=="off":
        print("Machine Turned off. Thank you for using coffee machine")
        os._exit(0)
    if Choice=="report":
        print(f"Water : {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} gm\nMoney: ${resources['money']}")
    else:
        if resources['water'] <= MENU[Choice]['ingredients']['water']:
            print("Sorry there is not enough water")
        elif resources['coffee'] <= MENU[Choice]['ingredients']['coffee']:
            print("Sorry there is not enough coffee")
        else:
            print(f"Cost of {Choice} is ${MENU[Choice]['cost']}")
            print("Insert Coins : ")
            quarters=int(input("How many quarters?"))
            dimes=int(input("How many dimes?"))
            pennies=int(input("How many pennies?"))
            nickels=int(input("How many nickels?"))
            dollars = (quarters * 0.25) + (dimes * 0.10) + (pennies * 0.01) + (nickels * 0.05)
            print(f"Total money inserted : ${round(dollars,2)}")
            if dollars < MENU[Choice]['cost']:
                print("Sorry that's not enough money. Money refunded")
                continue
            elif dollars == MENU[Choice]['cost']:
                resources['money'] += dollars
                print(f"Here's your {Choice} Enjoy!!")
            else:
                change = dollars - MENU[Choice]['cost']
                print(f"Here is ${round(change,2)} dollars in change. ")
                resources['money'] += MENU[Choice]['cost']
                print(f"Here's your {Choice} Enjoy!!")
            if Choice == "latte" or Choice == "cappuccino":
                resources['milk'] -= MENU[Choice]['ingredients']['milk']
            resources['water'] -= MENU[Choice]['ingredients']['water']

            resources['coffee'] -= MENU[Choice]['ingredients']['coffee']
