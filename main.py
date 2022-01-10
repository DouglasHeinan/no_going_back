from classes import warrior, battle_mage, soldier, berserker


CLASS_LIST = [warrior]
SUB_CLASS_LIST = [battle_mage, soldier, berserker]


def main():
    player_class, sub_class = intro()
    # establish character
    # choose island
    # proceed through island


def intro():
    """At the start of a new game, intro() will run to prompt the user to create and name a character."""
    print("Welcome to 'No Going Back'!")
    print("This is a text-based fantasy adventure.")
    print("To begin, choose your adventurer's class:")
    print(f"1. {CLASS_LIST[0]['Class']}")
    player_class = input("Which class would you like to play as? (Select the number that corresponds to your "
                         "preferred class.) ")
    player_class = check_class(player_class, CLASS_LIST)
    player_class = CLASS_LIST[player_class - 1]
    sub_class = sub_class_selection()
    print(f"You've chosen to play as a {player_class['Class']} {sub_class['Class']}")
    return player_class, sub_class


def sub_class_selection():
    print("Choose your sub-class:")
    for job in SUB_CLASS_LIST:
        index = 
        print(f"{SUB_CLASS_LIST[index] - 1}. {job}")
    sub_class = input("Which sub_class would you like to play as? (Select the number that corresponds to your preferred"
                      "class) ")
    sub_class = check_class(sub_class, SUB_CLASS_LIST)
    sub_class = SUB_CLASS_LIST[sub_class - 1]
    return sub_class


def check_class(player_class, player_class_list):
    """This function runs during the intro function. It verifies that the user entry for class or sub_class type is
    valid."""
    while not player_class.isdigit() or int(player_class) > len(player_class_list) or int(player_class) < 1:
        print("Please choose from the available options.")
        player_class = input("Which class would you like to play as? (Select the number that corresponds to your "
                             "preferred class.) ")
    return int(player_class)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
