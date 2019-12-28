from player_fight import *

p1 = Player('p1')
p2 = Player('p2')
while True:
    if p1.hp >= 0:
        p1.attack(p2)
        if p2.hp >= 0:
            p2.attack(p1)
        else:
            print(p2.name, 'was defeated by', p1.name)
            break
    else:
        print(p1.name, 'was defeated by', p2.name)
        break
