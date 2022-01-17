ALL_ITEMS = ["torch", "healing potion"]
"""Manages items and item usage for the adventure"""


class Items:
    def __init__(self, sub_class):
        self.items = {"Slot 1": "empty", "Slot 2": "empty", "Slot 3": "empty", "Slot 4": "empty", "Slot 5": "empty"}
        self.torch_on = False
        for item in range(len(sub_class["Items"])):
            num = item + 1
            self.items[f"Slot {num}"] = sub_class["Items"][item]

    def inventory(self):
        print("These are your items:")
        for item in self.items:
            print(f"{item}: {self.items[item]}")
        print("")

    def choose_item(self):
        for item in self.items:
            print(f"{item}: {self.items[item]}")
        item_slot = input("Which item would you like to use? (Select the corresponding number; "
                          "Press 'Enter' to cancel) ")
        if item_slot == "":
            print("")
            return
        while not item_slot.isdigit() or int(item_slot) < 1 or int(item_slot) > 5 or self.items[f"Slot {item_slot}"] == "empty":
            print("Please enter a valid number.")
            item_slot = input("Which item would you like to use? (Select the corresponding number) ")
        to_use = self.items[f"Slot {item_slot}"]
        self.items[f"Slot {item_slot}"] = "empty"
        print("")
        return to_use

    def use_item(self, item, hp, sub_class):
        if item == "torch":
            self.torch()
        if item == "healing potion":
            hp = self.healing_potion(hp, sub_class)

    def torch(self):
        print("You have lit one of your torches")
        print("")
        self.torch_on = True

    def healing_potion(self, hp, sub_class):
        hp += 5
        if hp > int(sub_class["Max_HP"]):
            hp = int(sub_class["Max_HP"])
        print(f"You now have {hp} hit points.")
        print("")
        return hp


