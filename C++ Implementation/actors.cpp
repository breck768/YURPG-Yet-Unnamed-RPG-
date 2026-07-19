//Class method definitions
#pragma once

#include "actors.h"
#include "defines.h"

Player::Player(string name, int job)
{
    editName(name);

    switch (job) //Used to assign default stats and equipment
    {
        case WARRIOR:
            editMaxHealth(50);
            editMaxMana(0);
            editHealth(50);
            editMana(0);

            editStrength(10);
            editDefense(10);
            editMagicDefense(5);
            editSpeed(5);
            editMagic(1);

            editWeapon("Sword");
            editArmor("Chestplate");
            editAccessory("Armband");

            break;
        case MAGE:
            editMaxHealth(20);
            editMaxMana(20);
            editHealth(20);
            editMana(20);

            editStrength(3);
            editDefense(2);
            editMagicDefense(10);
            editSpeed(3);
            editMagic(10);

            editWeapon("Staff");
            editArmor("Leather Shirt");
            editAccessory("Necklace");

            break;
        case ROGUE:
            editMaxHealth(40);
            editMaxMana(0);
            editHealth(40);
            editMana(0);

            editStrength(6);
            editDefense(6);
            editMagicDefense(5);
            editSpeed(10);
            editMagic(1);

            editWeapon("Knife");
            editArmor("Leather Shirt");
            //editAccessory(""); No default accessory

            break;
        default:
            std::cout << "invalid job lol";
            //should validate job before calling constructor
            break;
    }
}

//Actor mutators
void Actor::editName(string val)
{
    this->name = val;
}
void Actor::editMaxHealth(int val)
{
    this->maxHealth = val;
}
void Actor::editMaxMana(int val)
{
    this->maxMana = val;
}
void Actor::editHealth(int val)
{
    this->health = val;
}
void Actor::editMana(int val)
{
    this->mana = val;
}
void Actor::editStrength(int val)
{
    this->strength = val;
}
void Actor::editDefense(int val)
{
    this->defense = val;
}
void Actor::editMagicDefense(int val)
{
    this->magicDefense = val;
}
void Actor::editSpeed(int val)
{
    this->speed = val;
}
void Actor::editMagic(int val)
{
    this->magic = val;
}

//Actor accessors
int Actor::getStrength()
{
    return this->strength;
}
int Actor::getDefense()
{
    return this->defense;
}

//Player mutators
void Player::editWeapon(string val)
{
    this->weapon = val;
}
void Player::editArmor(string val)
{
    this->armor = val;
}
void Player::editAccessory(string val)
{
    this->accessory = val;
}

//Player accessors
string Player::getWeapon()
{
    return weapon;
}
string Player::getArmor()
{
    return armor;
}


//Debug methods
void Actor::DEBUG_DUMPSTATS()
{
    cout << "hallo :D";
}

void Player::DEBUG_DUMPSTATS()
{
    cout << "name: " << name << endl;
    cout << "health: " << health << endl;
    cout << "max health: " << maxHealth << endl;
    cout << "mana: " << mana << endl;
    cout << "max mana: " << maxMana << endl << endl;
    cout << "strength: " << strength << endl;
    cout << "magic: " << magic << endl;
    cout << "defense: " << defense << endl;
    cout << "magic defense: " << magicDefense << endl;
    cout << "speed: " << speed << endl << endl;
    cout << "weakness: " << weakness << endl;
    cout << "resistant: " << resistant << endl;
    cout << "immune: " << immune << endl;
    cout << "absorb: " << absorb << endl << endl;
    cout << "level: " << level << endl;
    cout << "exp: " << exp << endl << endl;
    cout << "job: " << job << endl;
}
