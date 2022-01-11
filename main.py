from classes import warrior, battle_mage, soldier, berserker
from lands import lands
from items import Items
import random

"""
These constants are used when creating your character or choosing an action during the game
"""
CLASS_LIST = [warrior]
SUB_CLASS_LIST = [battle_mage, soldier, berserker]
NON_COMBAT_ACTIONS = ["1.Examine your inventory", "2.Use an item", "3.Use an ability", "4.Search",
                      "5.Check your status", "6.Travel", "7.Attack"]


def main():
    """
    The main program starts by letting the player choose which class and sub class they'd like to play as, then asking
    which sort of land they'd like to begin their journey in. It briefly introduces the character to their situation
    and their character and establishes their starting hp and items.
    """
    player_class, sub_class = intro()
    location = choose_land()
    hp = sub_class['Current_HP']
    start_area = intro_chooser()
    scenario = location[start_area]
    items = Items(sub_class)
    print(f"You are a {player_class['Class']} {sub_class['Class']} with {hp} hit points, adventuring through the "
          f"{location['Type']} of PlaceHolderLand.")
    """
    A few key words are established before the main event runs.
    """
    game_over = False
    combat = False
    current_area = scenario
    print(current_area)
    """
    For as long as the game isn't over (i.e., the player is not out of HP), the user is continually asked to 
    respond to prompts to move the game along.
    """
    while not game_over:
        action = user_input()
        if action == "1":
            items.inventory()
        elif action == "2":
            item_to_use = items.choose_item()
            items.use_item(item_to_use, hp, sub_class)


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
    """Let's the user select their sub-class, which determines most of their stats and starting abilities."""
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
    """Let's the user decide what terrain their game starts in."""
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


def intro_chooser():
    """Chooses a random starting scenario for the player"""
    intro_list = ["Intro1", "Intro2", "Intro3"]
    choice = random.choice(intro_list)
    return choice


def user_input():
    """Takes the user's input regarding an action to perform"""
    print("What would you like to do?")
    for action in NON_COMBAT_ACTIONS:
        print(action)
    choice = input("Select 1-7 ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 7:
        print("Please select a valid option.")
        choice = input("What would you like to do (Select 1-7) ")
    return choice


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
