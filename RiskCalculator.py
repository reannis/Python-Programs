import random as r
#import the random function
attackerarmys = int(input('enter number of attacking armys '))
defenderarmys = int(input('enter number of defending armys '))
#sets the initial number of armys

minimum_remainder = int(input('enter minimum number of remaining armys '))

while attackerarmys > minimum_remainder and defenderarmys > 0:
    die1 = r.randint(1,6)
    die2 = r.randint(1,6)
    die3 = r.randint(1,6)
    die4 = r.randint(1,6)
    die5 = r.randint(1,6)

    if attackerarmys == 2:
        attacker = [die1]
    elif attackerarmys == 3:
        attacker = [die1, die2]
    else:
        attacker = [die1, die2, die3]

    if defenderarmys == 1:
        defender = [die4]
    else:
        defender = [die4, die5]

    attacker.sort(reverse = True)
    defender.sort(reverse = True)
    #print(attacker)
    #print(defender)

    if len(attacker) > 1 and len(defender) > 1:
        attacker1_win = attacker[0] > defender[0]
        attacker2_win = attacker[1] > defender[1]

        if attacker1_win and attacker2_win == True:
            defenderarmys = defenderarmys - 2
        elif attacker2_win == True and attacker1_win == False:
            attackerarmys = attackerarmys - 1
            defenderarmys = defenderarmys - 1
        elif attacker2_win == False and attacker1_win == True:
            attackerarmys = attackerarmys - 1
            defenderarmys = defenderarmys - 1
        else:
            attackerarmys = attackerarmys - 2
    else:
        attacker1_win = attacker[0] > defender[0]
        if attacker1_win == True:
            defenderarmys -= 1
        else:
            attackerarmys -= 1
#print(attackerarmys)

if not (attackerarmys >= 0):
    attackerarmys = 0
    
if attackerarmys > defenderarmys:
    print("Attackers Win")
else:
    print("Defenders Win")
    
print(attackerarmys, 'attacker armys left')
print(defenderarmys, 'defender armys left')

