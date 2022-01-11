ALL_ITEMS = ["torch", "healing potion"]
"""Manages items and item usage for the adventure"""


class Items:
    def __init__(self, sub_class):
        self.items = []
        self.torch_on = False
        for item in sub_class["Items"]:
            self.items.append(item)

    def inventory(self):
        print("These are your items:")
        for item in self.items:
            print(item)

    def choose_item(self):
        num = 0
        for item in self.items:
            num += 1
            print(f"{num}. {item}")
        to_use = input("Which item would you like to use? (Select the corresponding number) ")
        while not to_use.isdigit() or int(to_use) < 1 or int(to_use) > num:
            print("Please enter a valid number.")
            input("Which item would you like to use? (Select the corresponding number) ")
        to_use = self.items[int(to_use) - 1]
        self.items.remove(to_use)
        return to_use

    def use_item(self, item, hp, sub_class):
        if item == "torch":
            self.torch()
        if item == "healing potion":
            hp = self.use_healing_potion(hp, sub_class)

    def torch(self):
        print("You have lit one of your torches")
        self.torch_on = True

    def use_healing_potion(self, hp, sub_class):
        hp += 5
        if hp > int(sub_class["Max_HP"]):
            hp = int(sub_class["Max_HP"])
        print(f"You now have {hp} hit points.")
        return hp


