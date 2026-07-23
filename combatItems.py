from combatDefines import *

class Weapon:
    attack = 0
    element = NONE

class Armor:
    defense = 0
    element = NONE

weaponDict = {}
armorDict = {}

def weaponInit():
    Sword = Weapon()
    Sword.attack = 4
    weaponDict["Sword"] = Sword

def armorInit():
    Chestplate = Armor()
    Chestplate.defense = 4
    armorDict["Chestplate"] = Chestplate

