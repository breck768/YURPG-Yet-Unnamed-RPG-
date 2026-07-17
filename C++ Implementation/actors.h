//Class definitions
#pragma once

#include "defines.h"

//File containing all actor objects (base actor object, player object, enemy objects)

class Actor
{
public:
    void editName(string val);

    //Used directly when using attack functions
    void editHealth(int val);
    void editMana(int val);

    //Used to edit stats (when equipping weapons/armor etc or when levelling up)
    void editMaxHealth(int val);
    void editMaxMana(int val);
    void editStrength(int val);
    void editDefense(int val);
    void editMagicDefense(int val);
    void editSpeed(int val);
    void editMagic(int val);

    //Query functions for attack formulas
    int getStrength();
    int getDefense();

    //Debug
    virtual void DEBUG_DUMPSTATS();

protected:
    string name;

    //Health values
    int health = 0;
    int maxHealth = 0;
    int mana = 0;
    int maxMana = 0;

    //General stats
    int strength = 0;
    int magic = 0; //Magic strength
    int defense = 0;
    int magicDefense = 0;
    int speed = 0; //Used in determining move order

    //Misc stats (use elemental macros here)
    int weakness = 0; //Double damage
    int resistant = 0; //Half damage
    int immune = 0; //No damage
    int absorb = 0; //Heal damage amount 

    //Stats unrelated to singular battles
    int level = 0;
    int exp = 0;

    vector<void*> attacks; //Attacks are currently implemented as functions that define their damage formulas.
    // As such, to determine if an actor can use a particular attack or spell, insert a function pointer into this vector.
    // Will likely spread them out into separate action/magic vectors for ease of use in menuing later.
};

class Player : public Actor //Definition for Players
{
public:
    Player(string name, int job);

    void editWeapon(string val);
    void editArmor(string val);
    void editAccessory(string val);

    string getWeapon();
    string getArmor();

    void DEBUG_DUMPSTATS() override;

private:
    int job = 0;
    //Equipment variables are the names of the equipment.
    //Equipment names serve as keys for a hashmap containing structs that define behavior and stats.

    string weapon = "";
    string armor = "";
    string accessory = "";
};

class Goblin : public Actor //All remaining class definitions are for enemy types
{
private:
    string name = "Goblin";
    int health = 10;
    int maxHealth = 10;

    int strength = 2;
    int speed = 1;

    int weakness = FIRE; 

    int level = 1;
};