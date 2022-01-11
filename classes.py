"""
'Description': ,
'Strength': ,
'Agility': ,
'Constitution': ,
'Intelligence': ,
'Wisdom': ,
'Perception': ,
'Speed': ,
'Max_HP': ,
'Current_HP': ,
'Potential_Abilities': [],
'Abilities': [],
'Potential_Spells': [],
'Spells': [],
'Items': [healing_potion, torch],
'Battle-Actions': [attack, use_ability, use_spell, use_item],
'Actions': [search, use]
"""


'''
Companions:
'''


apprentice_wizard = {
    'Name': '',
    'Class': 'Wizard',
    'Description': 'A young wizard, still coming up in the ranks.',
    'Strength': -2,
    'Agility': 0,
    'Constitution': 0,
    'Intelligence': 3,
    'Wisdom': 0,
    'Perception': 2,
    'Speed': 2,
    'Max_HP': 5,
    'Current_HP': 5,
    'Potential_Abilities': [],
    'Abilities': [],
    'Potential_Spells': ['healing', 'fire_ball', 'ice_armor'],
    'Spells': ['fire_bolt', 'ice_bolt'],
    'Items': ['healing_potion'],
    'Battle-Actions': ['attack', 'use_ability', 'use_spell', 'use_item'],
    'Actions': ['search', 'use']
}
healing_deacon = {
    'Name': '',
    'Class': 'Healer',
    'Description': 'A youthful priest, eager to do good in the world. Bit of a chicken, though...',
    'Strength': 0,
    'Agility': 0,
    'Constitution': -1,
    'Intelligence': 0,
    'Wisdom': 3,
    'Perception': 1,
    'Speed': 2,
    'Max_HP': 4,
    'Current_HP': 4,
    'Potential_Abilities': [],
    'Abilities': [],
    'Potential_Spells': [],
    'Spells': ['healing', 'prayer_of_protection'],
    'Items': ['healing_potion', 'torch'],
    'Battle-Actions': ['attack', 'use_ability', 'use_spell', 'use_item'],
    'Actions': ['search', 'use']
}
sneaky_pal = {
    'Name': '',
    'Class': 'Sneak',
    'Description': 'A sly thief, used to going unnoticed on the fringes.',
    'Strength': 0,
    'Agility': 2,
    'Constitution': 0,
    'Intelligence': 0,
    'Wisdom': 0,
    'Perception': 2,
    'Speed': 3,
    'Max_HP': 5,
    'Current_HP': 5,
    'Potential_Abilities': [],
    'Abilities': ['dagger_throw', 'lockpick'],
    'Potential_Spells': [],
    'Spells': [],
    'Items': ['healing_potion', 'torch'],
    'Battle-Actions': ['attack', 'use_ability', 'use_spell', 'use_item'],
    'Actions': ['search', 'use']
}

battle_mage = {
    'Class': 'Battle Mage',
    'Description': 'Wields a one-handed weapon in one hand and keeps off-hand free to cast spells on said weapon or'
                   'launch ranged magical attacks.',
    'Strength': 3,
    'Agility': 0,
    'Constitution': 2,
    'Intelligence': 2,
    'Wisdom': 0,
    'Perception': -1,
    'Speed': 2,
    'Max_HP': 12,
    'Current_HP': 12,
    'Defense': 0,
    'Potential_Abilities': [],
    'Abilities': [],
    'Potential_Spells': ['magic armor', 'ethereal shield', 'fireworks', 'warrior spell', 'flaming sword', 'fire ball',
                         'icy blast', 'frozen sword', 'downpour'],
    'Spells': ['magic bolt'],
    'Items': ['healing potion', 'torch'],
    'Battle-actions': ['attack', 'use_ability', 'use_spell', 'use_item'],
    'Actions': ['search', 'use']
    }

soldier = {
    'Class': 'Soldier',
    'Description': 'Trained in a variety of combat styles, can use one-handed weapons with a shield or cross-bows',
    'Strength': 2,
    'Agility': 2,
    'Constitution': 2,
    'Intelligence': 0,
    'Wisdom': 0,
    'Perception': 0,
    'Speed': 3,
    'Max_HP': 13,
    'Current_HP': 13,
    "Defense": 0,
    'Potential_Abilities': ['two_arrows', 'move_silently', 'quick_slice', 'steady_hand', 'defensive_stance',
                            'quick_shot'],
    'Abilities': ['power_shot', 'power_strike'],
    'Potential_Spells': [],
    'Spells': [],
    'Items': ['healing_potion', 'torch'],
}
berserker = {
    'Class': 'Berserker',
    'Description': 'A ruthless killing machine that can go into a violent, trance-like state '
                   'where abilities are heightened and damage is increased. Uses two-handed melee weapons.',
    'Strength': 3,
    'Agility': 2,
    'Constitution': 3,
    'Intelligence': -1,
    'Wisdom': 0,
    'Perception': -1,
    'Speed': 2,
    'Max_HP': 15,
    'Current_HP': 15,
    'Defense': 0,
    'Potential_Abilities': ['advanced berserk', 'mega rage', 'power strike', 'charge', 'quick strikes', 'bash',
                            'advanced bash', 'leap attack', 'trance'],
    'Abilities': ['berserk'],
    'Potential_Spells': ['disarm', 'fire blade', 'flame armor'],
    'Spells': ['regeneration'],
    'Items': ['healing potion', 'torch'],
    'Battle-Actions': ['attack', 'use ability', 'use spell', 'use item'],
    'Actions': ['search', 'use']
}
warrior = {
    'name': '',
    'Class': 'Warrior',
    'Sub-classes': [battle_mage, soldier, berserker],
    'Companion-options': [apprentice_wizard, healing_deacon, sneaky_pal]
}
# wizard = {
#     'name': '',
#     'class': 'Wizard',
#     'Sub-classes': [druid, illusionist, elementalist],
#     'Companion-options': [tanky-swordster, nimble_attack_dog, sneaky_pal]
# }
# elementalist = {
#     'Description': 'A magic-user with a plethora of offensive attacks. Carries a wand in main-hand.',
#     'Strength': -1,
#     'Agility': 2,
#     'Constitution': 1,
#     'Intelligence': 5,
#     'Wisdom': -1,
#     'Perception': -1,
#     'Speed': 2,
#     'Max_HP': 7,
#     'Current_HP': 7,
#     'Potential_Abilities': [],
#     'Abilities': [],
#     'Potential_Spells': [fire_shot, fire_ball, ice_shot, ice_blast, teleport, wizard_lightning, ice_armor, fire_armor,
#                          invisibility, healing, rain_of_fire, healing_rain, ],
#     'Spells': [magic_bolt, illumination],
#     'Items': [healing_potion],
#     'Battle-Actions': [attack, use_ability, use_spell, use_item],
#     'Actions': [search, use]
# }
# illusionist = {
# 'Description': 'A sneaky wizard who focuses on confusing his opponent and pitting enemies against one another.
# Carries a wand in main hand.',
# 'Strength': -1,
# 'Agility': 0,
# 'Constitution': 0,
# 'Intelligence': 3,
# 'Wisdom': 1,
# 'Perception': 3,
# 'Speed': 2,
# 'Max_HP': 7,
# 'Current_HP': 7,
# 'Potential_Abilities': [],
# 'Abilities': [dazzling_lights, ],
# 'Potential_Spells': [invisibility, calm, decoy, faux_ally, stun, fire_trap, icy_trap, suggestion, enrage, ],
# 'Spells': [pacify,],
# 'Items': [healing_potion],
# 'Battle-Actions': [attack, use_ability, use_spell, use_item],
# 'Actions': [search, use]
# }
# druid = {
# 'Description': 'A wizard more in touch with the natural world. Can take the form of some wild animals and summon '
#                'others. Better in battle than most wizards; can use bow and arrow',
# 'Strength': 0,
# 'Agility': 1,
# 'Constitution': 0,
# 'Intelligence': 0,
# 'Wisdom': 3,
# 'Perception': 3,
# 'Speed': 2,
# 'Max_HP': 9,
# 'Current_HP': 9,
# 'Potential_Abilities': [],
# 'Abilities': [call_of_the_wild, summon_hawk, summon_elk],
# 'Potential_Spells': [transform_squirrel, transform_bear],
# 'Spells': [transform_wolf],
# 'Items': [healing_potion, torch],
# 'Battle-Actions': [attack, use_ability, use_spell, use_item],
# 'Actions': [search, use]
# }
# rogue = {
#     'name': '',
#     'class': 'Rogue',
#     'Sub-class': [ranger, bandit, assassin],
#     'Companion-options': [attack_dog, apprentice_wizard, rodent_companion]
# }
# bandit = {
#     'Description': 'A sly thief, adept at'
#     'Strength': -1,
#     'Agility': 2,
#     'Constitution': 0,
#     'Intelligence': 1,
#     'Wisdom': 1,
#     'Charisma': 2,
#     'Perception': 1,
#     'Speed': 5,
#     'Max_HP': 0,
#     'Current_HP': 0,
#     'Potential_Abilities': [],
#     'Abilities': [],
#     'Potential_Spells': [],
#     'Spells': [],
#     'Items': [healing_potion]
# }
# cleric = {
#     'name': '',
#     'class': 'Cleric',
#     'Sub-class': [pious, demon_slayer, necromancer]
#     'Strength': 1,
#     'Agility': 0,
#     'Constitution': 2,
#     'Intelligence': 0,
#     'Wisdom': 3,
#     'Charisma': 0,
#     'Perception': 0,
#     'Speed': 2,
#     'Max_HP': 0,
#     'Current_HP': 0,
#     'Potential_Abilities': [],
#     'Abilities': [],
#     'Potential_Spells': [],
#     'Spells': [],
#     'Items': [healing_potion]
# }
# necromancer = {
# raise_dead, raise_hulking_dead, conjure_skeletal_aid, circle_of_protection
# }
#
# ranger = {
#     'name': '',
#     'class': 'Ranger',
#     'Strength': 1,
#     'Agility': 3,
#     'Constitution': 0,
#     'Intelligence': 0,
#     'Wisdom': 1,
#     'Charisma': -2,
#     'Perception': 3,
#     'Speed': 4,
#     'Max_HP': 0,
#     'Current_HP': 0,
#     'Potential_Abilities': [],
#     'Abilities': [],
#     'Potential_Spells': [],
#     'Spells': [],
#     'Items': [healing_potion]
# }
# bard = {
#     'name': '',
#     'class': 'Bard',
#     'Strength': -2,
#     'Agility': 0,
#     'Constitution': 0,
#     'Intelligence': 1,
#     'Wisdom': 2,
#     'Charisma': 3,
#     'Perception': 2,
#     'Speed': 3
#     'Max_HP': 0,
#     'Current_HP': 0,
#     'Potential_Abilities': [],
#     'Abilities': [],
#     'Potential_Spells': [],
#     'Spells': [],
#     'Items': [healing_potion]
# }
