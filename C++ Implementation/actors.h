//Class definitions
#pragma once

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
    void editDefense(int val);
    void editMagicDefense(int val);
    void editSpeed(int val);
    void editMagic(int val);

private:
    string name;

    //Health values
    int health;
    int maxHealth;
    int mana;
    int maxMana;

    //General stats
    int strength;
    int magic; //Magic strength
    int defense;
    int magicDefense;
    int speed; //Used in determining move order

    //Misc stats (use elemental macros here)
    int weakness; //Double damage
    int resistant; //Half damage
    int immune; //No damage
    int absorb; //Heal damage amount 

    //Stats unrelated to singular battles
    int level;
    int exp;

    vector<void*> attacks; //Attacks are currently implemented as functions that define their damage formulas.
    // As such, to determine if an actor can use a particular attack or spell, insert a function pointer into this vector.
    // Will likely spread them out into separate action/magic vectors for ease of use in menuing later.
};

class Player : public Actor 
{
public:
    Player(string name, int job);
    void editWeapon(string val);
    void editArmor(string val);
    void editAccessory(string val);

private:
    //Equipment variables are the names of the equipment.
    //Equipment names serve as keys for a hashmap containing structs that define behavior and stats.
    string weapon;
    string armor;
    string accessory;
};

class Enemy : public Actor
{
public:

private:

};