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

    Staff = Weapon()
    Staff.attack = 1
    weaponDict["Staff"] = Staff

def armorInit():
    Chestplate = Armor()
    Chestplate.defense = 4
    armorDict["Chestplate"] = Chestplate

    Shirt = Weapon()
    Shirt.defense = 1
    armorDict["Shirt"] = Shirt

