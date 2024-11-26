import copy
import cards
currently_selected = None
kit_list = {'kit1': {'name': 'martin', 'hp': 250, 'strength': 80, 'endurance': 10}}
characters = dict(Eclipse=cards.Eclipse, Havoc=cards.Havoc, Ironclad=cards.Ironclad, BlaseFury=cards.BlazeFury,
                  Guardian=cards.Guardian, ShardSpire=cards.ShardSpire, JadeFang=cards.JadeFang,
                  Dreadnought=cards.Dreadnought, Aegis=cards.Aegis, FrostBlade=cards.FrostBlade)


def set_name(kit, name=None):
    if name is None:
        while True:
            try:
                name = str(input("what's the name of the character ? "))
                break
            except ValueError:
                print("Please enter a valid string.")
            except EOFError:
                print("Input ended unexpectedly.")
                break
    new_character = copy.deepcopy(kit_list[kit])
    new_character['name'] = name
    characters[name] = new_character
    return characters


def hp_change(name, hp_to_change):
    name['hp'] = name['hp'] + hp_to_change
    return name


def printing_status(name):
    named = characters[name]
    for key, value in named.items():
        print(key, ':', value)


def attack(attacker, attacked):
    hp_change(attacked, (0-attacker['strength']))
    attacker['endurance'] = attacker['endurance']-2
    return attacked, attacker


def character_change(name=None):
    global currently_selected
    if name is None:
        while True:
            try:
                name = str(input("Which character do you want to pick ?"))
                break
            except ValueError:
                print("please enter a valid name ")
            except EOFError:
                print("unexpected input ")
                break
        if name in characters:
            currently_selected = name
            return currently_selected
        else:
            set_name('kit1', name)
            currently_selected = name
            return currently_selected
    else:
        if name in characters:
            currently_selected = name
            return currently_selected
        else:
            set_name('kit1', name)
            currently_selected = name
            return currently_selected
