NON_COMBAT_ACTIONS = ["1.Examine your inventory", "2.Use an item", "3.Use an ability", "4.Search",
                      "5.Check your status", "6.Travel", "7.Attack"]


class Input:
    def __init__(self, combat, action, sub_class):
        if not combat:
            if action == "1":
                self.inventory(sub_class)

    def inventory(self, sub_class):
        print("These are your items:")
        for item in sub_class["Items"]:
            print(item)
