from __future__ import print_function
from pprint import pprint
import json
from unit import *
from types import SimpleNamespace


p1 = Datasheet_Profiles("troops","NECRON WARRIORS","5''",3,3,4,4,1,1,10,4,"none")
p2 = Datasheet_Profiles("troops","Cadian Shock Troops","6''",4,4,3,3,1,1,6,5,"-")

w1 = Datasheet_Weapons("Plasma Cannon",14,"Range",7,6,1,[])
w2 = Datasheet_Weapons("Lasgun",10,"Range",5,4,2,[])

necro1 = Datasheet_Unit("Necrons",p1,w1)
guard1 = Datasheet_Unit("Imperial Guard",p2,w2)

def toJSON(unit):
    junitPr = json.dumps(unit.Profile.__dict__)
    junitWp = json.dumps(unit.Weapons.__dict__)
    jsonobj = {"Race":unit.Race,
        "Profile":unit.Profile.__dict__,
        "Weapons":unit.Weapons.__dict__}
    return json.dumps(jsonobj)

def jsonToFile(junit, jname):
    f = open("./units/"+jname+".json", "w")
    f.write(junit)
    f.close()

def jsonFromFile(jname):
    f = open("./units/"+jname+".json", "r")
    jdata = json.loads(f.read())
    return jdata

def fromJSON(junit):
    jrace = junit['Race']
    jPr = Datasheet_Profiles(
        junit['Profile']['Battlefield_role'],
        junit['Profile']['Name'],
        junit['Profile']['Movement'],
        junit['Profile']['Weapon_Skill'],
        junit['Profile']['Ballistic_Skill'],
        junit['Profile']['Strength'],
        junit['Profile']['Toughness'],
        junit['Profile']['Wounds'],
        junit['Profile']['Attacks'],
        junit['Profile']['Leadership'],
        junit['Profile']['Armour_Save'],
        junit['Profile']['Abilites'])
    jWp = Datasheet_Weapons(
        junit['Weapons']['Name'],
        junit['Weapons']['Range'],
        junit['Weapons']['Type'],
        junit['Weapons']['Strength'],
        junit['Weapons']['Armour_Penetration'],
        junit['Weapons']['Damage'],
        junit['Weapons']['Abilites'])
    unit = Datasheet_Unit(jrace,jPr,jWp)
    return unit
