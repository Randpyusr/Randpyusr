import copy
currently_selected = None
kit_list = {'kit1': {'name': 'martin', 'hp': 250, 'strenght': 80, 'endurance': 10}}
caracters = {}


def set_name(kit, name=None):
    if name is None:
        name = input('quel est le nom du personnage ? ')
    new_caracter = copy.deepcopy(kit_list[kit])
    new_caracter['name'] = name
    caracters[name] = new_caracter
    return caracters


def hp_change(name, hp_to_change):
    name['hp'] = name['hp'] + hp_to_change
    return name


def printing_status(name):
    named = caracters[name]
    for key, value in named.items():
        print(key, ':', value)


def attack(attacker, attacked):
    hp_change(attacked, (0-attacker['strenght']))
    attacker['endurance'] = attacker['endurance']-2
    return attacked, attacker


def caracter_change(name=None):
    global currently_selected
    if name is None:
        name = input("quel est le nom du personnage que vous voulez sélectionner ?")
        if name in caracters:
            currently_selected = name
            return currently_selected
        else:
            set_name('kit1', name)
            currently_selected = name
            return currently_selected
    else:
        if name in caracters:
            currently_selected = name
            return currently_selected
        else:
            set_name('kit1', name)
            currently_selected = name
            return currently_selected


class Object:

    def __init__(self, hp_effect, strenght_effect, endurance_effect):
        self.hp_effect = hp_effect
        self.strenght_effect = strenght_effect
        self.endurance_effect = endurance_effect

    @staticmethod
    def object_hp(hp_effect):
        hp_change(caracters[currently_selected], hp_effect)

    @staticmethod
    def object_strenght(strenght_effect):
        caracters[currently_selected]['strenght'] += strenght_effect

    @staticmethod
    def object_endurance(endurance_effect):
        caracters[currently_selected]['endurance'] += endurance_effect
