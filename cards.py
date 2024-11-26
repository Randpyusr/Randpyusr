import shared


class Object:

    def __init__(self, hp_effect, strength_effect, endurance_effect):
        self.hp_effect = hp_effect
        self.strength_effect = strength_effect
        self.endurance_effect = endurance_effect

    @staticmethod
    def object_hp(hp_effect):
        shared.hp_change(characters[shared.currently_selected], hp_effect)

    @staticmethod
    def object_strength(strength_effect):
        characters[shared.currently_selected]['strength'] += strength_effect

    @staticmethod
    def object_endurance(endurance_effect):
        characters[shared.currently_selected]['endurance'] += endurance_effect


class Hero:
    def __init__(self, name, strength, hp, endurance):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.endurance = endurance


# Hero creation
Eclipse = Hero(name='Eclipse', strength=15, hp=73, endurance=10)
Ironclad = Hero(name='Ironclad', strength=12, hp=88, endurance=7)
BlazeFury = Hero(name='BlazeFury', strength=18, hp=64, endurance=14)
Guardian = Hero(name='Guardian', strength=10, hp=92, endurance=6)
ShardSpire = Hero(name='ShardSpire', strength=20, hp=55, endurance=12)
JadeFang = Hero(name='JadeFang', strength=13, hp=81, endurance=9)
Dreadnought = Hero(name='Dreadnought', strength=14, hp=75, endurance=11)
Aegis = Hero(name='Aegis', strength=11, hp=90, endurance=5)
Havoc = Hero(name='Havoc', strength=19, hp=50, endurance=15)
FrostBlade = Hero(name='FrostBlade', strength=16, hp=66, endurance=13)

characters = dict(Eclipse=Eclipse, Havoc=Havoc, Ironclad=Ironclad, BlaseFury=BlazeFury,
                  Guardian=Guardian, ShardSpire=ShardSpire, JadeFang=JadeFang,
                  Dreadnought=Dreadnought, Aegis=Aegis, FrostBlade=FrostBlade)
# healing cards
heal20 = Object(20, 0, 0)
heal30 = Object(30, 0, 0)
heal40 = Object(40, 0, 0)
heal50 = Object(50, 0, 0)

# strength cards
strength20 = Object(0, 20, 0)
strength30 = Object(0, 30, 0)
strength40 = Object(0, 40, 0)
strength50 = Object(0, 50, 0)

# endurance cards
endurance2 = Object(0, 0, 2)
endurance3 = Object(0, 0, 3)
endurance4 = Object(0, 0, 4)
endurance5 = Object(0, 0, 5)
