from combatDefines import *
from combatItems import *
import random

"""RNG DOCS:
random.randint() generates a random integer between the left and right values.
Left value can be as low as -100, right value does not have a limit.
After getting a random integer, it is divided by 100 to get a multiplier value.
1 is added to the value to guarantee it is positive, it is then multiplied with the calculated damage to get the final value

Examples of usage:
random.randomint(-50, 50)...
Floor becomes -0.5x, ceiling becomes 1.5x

random.randomint(-100, 100)...
Floor becomes 0x, ceiling becomes 2.
"""

def playerAttack(attacker, defender):
    damage = attacker.strength + weaponDict[attacker.weapon].attack - defender.defense
    randy = random.randint(-50, 50)
    mul = float(randy)/100
    mul += 1
    damage = damage * mul
    return int(damage)

def enemyAttack(attacker, defender):
    damage = attacker.strength - defender.defense - armorDict[defender.armor].defense
    randy = random.randint(-50, 50)
    mul = float(randy)/100
    mul += 1
    damage = damage * mul
    return int(damage)
