import copy
kit_list = {'kit1':{'name':'martin','hp':250,'strenght':80,'endurance':10}}
caracters = {}
def set_name(kit, kit_list):
    name = input('quel est le nom du personnage ? ')
    new_caracter=copy.deepcopy(kit_list[kit])
    new_caracter['name']=name
    caracters[name]=new_caracter
    return caracters

def hp_change(name,hp_to_change):
    name['hp'] = name['hp'] + hp_to_change
    return name

def printing_status(caracters,name):
    named = caracters[name]
    for key,value in named.items():
        print(key, ':', value)

def attack(attacker, attacked, strenght=None,):
    if strenght == None :
        strenght=attacker['strenght']
    hp_change(attacked,(0-attacker['strenght']))
    attacker['endurance'] = attacker['endurance']-2
    return attacked,attacker

class object :
    def __init__(self,hp_effect,strenght_effect,endurance_effect):
        self.hp_effect = hp_effect
        self.strenght_effect = strenght_effect
        self.endurance_effect = endurance_effect
    def object_hp(self,hp_effect):
        hp_change(caracters['pierre'],hp_effect)

    def object_strenght(self, strenght_effect):
        caracters['pierre']['strenght']+=strenght_effect
    def object_endurance(self,endurance_effect):
        caracters['pierre']['endurance']+=endurance_effect