from classes import warrior, battle_mage, soldier, berserker
from lands import lands


CLASS_LIST = [warrior]
SUB_CLASS_LIST = [battle_mage, soldier, berserker]


def main():
    player_class, sub_class = intro()
    location = choose_land()
    print(f"You are a {player_class['Class']} {sub_class['Class']}, adventuring through the {location['Type']} "
          f"locations of Gabagoo.")


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
        index = SUB_CLASS_LIST.index(job) + 1
        print(f"{index}. {job['Class']}: {job['Description']}")
    sub_class = input("Which sub_class would you like to play as? (Select the number that corresponds to your preferred"
                      " class) ")
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


def choose_land():
    num = 1
    print("Where do you feel like adventuring:")
    for land in lands:
        print(f"{num}. {land['Type']}")
        num += 1
    land = input("Choose a region to journey through: ")
    while not land.isdigit() or int(land) < 0 or int(land) > 8:
        print("Please enter a valid response.")
        land = input("Choose a region to journey through: ")
    land = int(land)
    land = lands[land - 1]
    return land


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
