from Menu import *




def insert_coins():

    quarters = float(input("How many quarters would you like to insert? "))
    dimes = float(input("How many dimes would you like to insert? "))
    nickles = float(input("How many nickles would you like to insert "))
    pennies = float(input("How many pennies would you like to insert? "))
    value = quarters * (Coins["quarter"]) + dimes * (Coins["dime"]) + nickles * (Coins["nickle"]) + pennies * (
        Coins["pennie"])








Money = 0


cont = True


while cont == True:
    usr_input = input("WHat would you like? (espresso/latte/cappuccino)? \n to top up the ingredients type in top up: ")
    if usr_input == "report":
        for ingredient in resources:
            print(f"{ingredient}: {resources[ingredient]}")
        print(Money)

    if usr_input == "espresso":
        print(f"An espresso costs:")
        print(MENU["espresso"]["cost"])
        quarters = float(input("How many quarters would you like to insert? "))
        dimes = float(input("How many dimes would you like to insert? "))
        nickles = float(input("How many nickles would you like to insert "))
        pennies = float(input("How many pennies would you like to insert? "))
        value = quarters * (Coins["quarter"]) + dimes * (Coins["dime"]) + nickles * (Coins["nickle"]) + pennies * (
            Coins["pennie"])
        if value < MENU["espresso"]["cost"]:
            print("Insufficient value")
            break
        else:
            Money += value
        for ingredient in MENU["espresso"]["ingredients"]:
            print(ingredient)
            if resources[ingredient] < MENU["espresso"]["ingredients"][ingredient]:
                print("Insuffocient resources")

            resources[ingredient] = resources[ingredient] - MENU["espresso"]["ingredients"][ingredient]

    if usr_input == "latte":
        print(f"A latte costs:")
        print(MENU["latte"]["cost"])
        quarters = float(input("How many quarters would you like to insert? "))
        dimes = float(input("How many dimes would you like to insert? "))
        nickles = float(input("How many nickles would you like to insert "))
        pennies = float(input("How many pennies would you like to insert? "))
        value = quarters * (Coins["quarter"]) + dimes * (Coins["dime"]) + nickles * (Coins["nickle"]) + pennies * (
            Coins["pennie"])
        if value < MENU["latte"]["cost"]:
            print("Insufficient value")
            break
        else:
            Money += value
        for ingredient in MENU["latte"]["ingredients"]:
            print(ingredient)
            if resources[ingredient] < MENU["latte"]["ingredients"][ingredient]:
                print("Insuffocient resources")

            resources[ingredient] = resources[ingredient] - MENU["latte"]["ingredients"][ingredient]

    if usr_input == "cappuccino":
        print(f"A cappuccino costs:")
        print(MENU["cappuccino"]["cost"])
        quarters = float(input("How many quarters would you like to insert? "))
        dimes = float(input("How many dimes would you like to insert? "))
        nickles = float(input("How many nickles would you like to insert "))
        pennies = float(input("How many pennies would you like to insert? "))
        value = quarters * (Coins["quarter"]) + dimes * (Coins["dime"]) + nickles * (Coins["nickle"]) + pennies * (
            Coins["pennie"])
        if value < MENU["cappuccino"]["cost"]:
            print("Insufficient value")
            break
        else:
            Money += value
        for ingredient in MENU["cappuccino"]["ingredients"]:
            print(ingredient)
            if resources[ingredient] < MENU["cappuccino"]["ingredients"][ingredient]:
                print("Insuffocient resources")

            resources[ingredient] = resources[ingredient] - MENU["cappuccino"]["ingredients"][ingredient]

    if usr_input == "top up":
        water_top_up = float(input("How much water would you like to add?: "))
        resources["water"] += water_top_up
        milk_top_up = float(input("How much milk would you like to add?: "))
        resources["milk"] += milk_top_up
        coffee_top_up = float(input("How much coffee would you like to add?: "))
        resources["coffee"] += coffee_top_up
        
   if usr_input = "quit":
        cont = False











