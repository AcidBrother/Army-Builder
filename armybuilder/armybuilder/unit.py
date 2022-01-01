from __future__ import print_function
from pprint import pprint
import json

class Datasheet_Unit:
    def __init__(self,
    Unit_Race,
    Unit_Profile,
    Unit_Weapons):
        self.Race = Unit_Race
        self.Profile = Unit_Profile
        self.Weapons = Unit_Weapons

class Datasheet_Profiles:
    def __init__(self,
    Profiles_Battlefield_role,
    Profiles_Name,
    Profiles_Movement,
    Profiles_Weapon_Skill,
    Profiles_Ballistic_Skill,
    Profiles_Strength,
    Profiles_Toughness,
    Profiles_Wounds,
    Profiles_Attacks,
    Profiles_Leadership,
    Profiles_Armour_Save,
    Profiles_Abilites):
        self.Battlefield_role = Profiles_Battlefield_role
        self.Name = Profiles_Name
        self.Movement = Profiles_Movement
        self.Weapon_Skill = Profiles_Weapon_Skill
        self.Ballistic_Skill = Profiles_Ballistic_Skill
        self.Strength = Profiles_Strength
        self.Toughness = Profiles_Toughness
        self.Wounds = Profiles_Wounds
        self.Attacks = Profiles_Attacks
        self.Leadership = Profiles_Leadership
        self.Armour_Save = Profiles_Armour_Save
        self.Abilites =  Profiles_Abilites

class Datasheet_Weapons:
    def __init__(self,
    Weapons_Name,
    Weapons_Range,
    Weapons_Type,
    Weapons_Strength,
    Weapons_Armour_Penetration,
    Weapons_Damage,
    Weapons_Abilites):
        self.Name = Weapons_Name
        self.Range = Weapons_Range
        self.Type = Weapons_Type
        self.Strength = Weapons_Strength
        self.Armour_Penetration = Weapons_Armour_Penetration
        self.Damage = Weapons_Damage
        self.Abilites = Weapons_Abilites

n1=Datasheet_Profiles("troops","NECRON WARRIORS","5''",3,3,4,4,1,1,10,4,"none")
n2=Datasheet_Profiles("troops","Cadian Shock Troops","6''",4,4,3,3,1,1,6,5,"-")
