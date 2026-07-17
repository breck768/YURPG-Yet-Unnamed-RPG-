//Attack functions take the attacker object as first argument and defender as second
//Returns damage dealt rather than applying damage.
#pragma once

#include "actors.cpp"
#include "items.h"

/* RNG DOCS:
The getRandNum function defined in defines.h generates a random integer between the left and right values.
Left value can be as low as -100, right value does not have a limit.
After getting a random integer, it is divided by 100 to get a multiplier value.
1 is added to the value to guarantee it is positive, it is then multiplied with the calculated damage to get the final value

Examples of usage:
getRandNum(-50, 50)...
Floor becomes -0.5x, ceiling becomes 1.5x

getRandNum(-100, 100)...
Floor becomes 0x, ceiling becomes 2.
*/

int basicAttack(Player *attacker, Actor *defender) //Player strength + Weapon attack - Enemy defense
{
    int damage = attacker->getStrength() + weaponMap.at(attacker->getWeapon()).attack - defender->getDefense();
    if (damage == 0) return 0;
    int randy = getRandNum(-50, 50);
    float mul = static_cast<float>(randy) / 100;
    mul += 1; 
    damage = damage * mul;
    return damage;
}

int basicAttack(Actor *attacker, Player *defender) //Enemy strength - Player defense - Armor defense
{
    int damage = attacker->getStrength() - defender->getDefense() - armorMap.at(defender->getArmor()).defense;
    if (damage == 0) return 0;
    int randy = getRandNum(-50, 50);
    float mul = static_cast<float>(randy) / 100;
    mul += 1; 
    damage = damage * mul;
    return damage;
}

int basicAttack(Actor *attacker, Actor *defender) //Attacker strength - Defender defense
{
    int damage = attacker->getStrength() - defender->getDefense();
    //if (damage <= 0) return 0;
    int randy = getRandNum(-50, 50); 
    float mul = randy / 100; 
    mul += 1;
    damage = damage * mul;
    return damage;
}