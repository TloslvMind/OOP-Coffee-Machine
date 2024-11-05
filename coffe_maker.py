class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources.
        :return: None """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resources_sufficient(self, drink):
        """
        :param drink: (MenuItem) The MenuItem object to make
        :return: True when the drink order can be made, False if ingredients are insufficient
        """
        can_make = True
        for item in drink.ingredients:
            if self.resources[item] < drink.ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make


    def make_coffee(self, order):
        """
        :param order: (MenuItem) The MenuItem object to make
        Deducts the required ingredients from the resources.
        :return: None """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
