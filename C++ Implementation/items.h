#pragma once

#include "defines.h"

struct Weapon
{
    int attack = 0;
    int element = NONE;
};

struct Armor
{
    int defense = 0;
    int element = NONE;
};

unordered_map<string, Weapon> weaponMap;
unordered_map<string, Armor> armorMap;

void weaponInit()
{
    Weapon Sword; //Create new weapons by creating a weapon object and edit the attributes
    {
        Sword.attack = 4; //doing it in this particular way has got to validate SOME kind of c++ standard but i dont care
    }
    weaponMap["Sword"] = Sword; //Add the weapon to the hash map 
}

void armorInit()
{
    Armor Chestplate;
    {
        Chestplate.defense = 4;
    }
    armorMap["Chestplate"] = Chestplate;
}