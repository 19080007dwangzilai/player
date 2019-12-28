import random


class Player:
    def __init__(self, name):
        self.ap = ''
        self.name = name
        self.hp = 100

    def attack(self, target):
        self.ap = random.randint(10, 20)
        print(self.name, 'is attacking ', target.name)
        target.hp = target.hp - self.ap

        if target.hp >= 0:
            print(target.name, 'of hp is', target.hp)
