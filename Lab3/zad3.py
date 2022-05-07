import random

from typing import List


class Monster:
    chance_to_upgrade = 0.1

    def __init__(self, name, hp, lvl, shield, attack):
        self.name = name
        if isinstance(hp, int):
            self.hp = hp
        else:
            raise TypeError

        if isinstance(lvl, int):
            self.lvl = lvl
        else:
            raise TypeError

        if isinstance(shield, int):
            self.shield = shield
        else:
            raise TypeError

        if isinstance(attack, int):
            self.attack = attack
        else:
            raise TypeError

    def att(self):
        return self.attack + random.randint(0,self.lvl) * self.attack

    def take_dmg(self, dmg):
        self.hp = self.hp + self.shield - dmg

    def uprgade(self):
        if (random.random() < self.chance_to_upgrade):
            self.lvl += 1

    def info(self):
        print("nazwa " + self.name + " hp " + str(self.hp) + " lvl "+ str(self.lvl) + " shield " + str(self.shield))

class Game:
    ile = 0
    list = []
    round = 0
    def __init__(self):
        self.list.append(Monster("komar",100,0,5,10))
        self.gracz = Monster("Gracz",100,5,0,30)


    def new(self):
        self.list.append(Monster("komar" + str(self.ile),100,0,5,10))



    def gameplay(self):
        while self.gracz.hp > 0:

            Monster.take_dmg(self.list[0],self.gracz.attack)
            Monster.info(self.list[0])
            if(self.list[0].hp < 0):
                self.ile+=1
                self.new()

            self.gracz.take_dmg(self.list[0].att())
            self.gracz.info()
            print("ILOŚC mobów pokonanych " + str(self.ile))
            self.round+=1





game = Game()

game.gameplay()
