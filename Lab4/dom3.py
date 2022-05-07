import random


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
        return self.attack + random.randint(0, self.lvl) * self.attack

    def take_dmg(self, dmg):
        self.hp = self.hp + self.shield - dmg

    def uprgade(self):
        if random.random() < self.chance_to_upgrade:
            self.lvl += 1

    def print(self):
        print("nazwa " + self.name + " hp " + str(self.hp) + " lvl " + str(self.lvl) + " shield " + str(self.shield))
        print(self.__class__.__name__)

class Game:
    _ile = 0
    list = []
    round = 0

    def __init__(self):
        self.list.append(Monster("komar", 100, 0, 5, 10))
        self.gracz = Monster("Gracz", 100, 5, 0, 30)

    @property
    def ile(self):
        return self._ile

    @ile.setter
    def ile(self, ile):
        if isinstance(ile, int):
            self._ile = ile
        else:
            raise TypeError

    @ile.deleter
    def ile(self):
        del self._ile

    def new(self):
        self.list.append(Monster("komar" + str(self.ile), 100, 0, 5, 10))

    def gameplay(self):
        while self.gracz.hp > 0:

            Monster.take_dmg(self.list[0], self.gracz.attack)
            Monster.info(self.list[0])
            if self.list[0].hp < 0:
                self.ile += 1
                self.new()

            self.gracz.take_dmg(self.list[0].att())
            self.gracz.info()
            print("ILOŚC mobów pokonanych " + str(self.ile))
            self.round += 1


# game = Game()
#
# game.gameplay()


class DINOZAURY_BEZ_NOSA_I_POWIEK(Monster):
    pass


class KOCZKODANY_CHOMIKOWATE(Monster):
    pass


class CEPY_I_GITAROMANGI(Monster):
    ilość_gitar = 3

    def attack(init):
        xd = super().att()
        return xd * 3


    def print(self):
        print("CEPY_I_GITAROMANGI")


class KOKOSO_GŁOWE(DINOZAURY_BEZ_NOSA_I_POWIEK):
    def print(self):
        print("KOKOSO_GŁOWE")




class DEKLASOROWNICY(CEPY_I_GITAROMANGI):
    ilość_gitar = 4
    pass

class JADOWITE_DZIKI_Z_HODOWLI(CEPY_I_GITAROMANGI):
    def __init__(self, name, hp, lvl, shield, attack,jadowitosc):
        super().__init__(name, hp, lvl,shield,attack)
        self.jadowitosc = jadowitosc
    def print(self):
        print("nazwa " + self.name + " hp " + str(self.hp) + " lvl " + str(self.lvl) + " shield " + str(self.shield)+ "jadowitosc" + str(self.jadowitosc))


if __name__ == '__main__':
    a = Monster("Jan", 10, 10, 10, 10)
    c1 = KOKOSO_GŁOWE("Arton", 20, 20, 20, 20)
    b2 = KOCZKODANY_CHOMIKOWATE("Jamik", 30, 30, 30, 30)
    b3 = CEPY_I_GITAROMANGI("Kokos", 40, 40, 40, 40)
    c4 = JADOWITE_DZIKI_Z_HODOWLI("muzyka", 50, 50, 50, 50, 50)
    b4 = DEKLASOROWNICY("Jan", 10, 10, 10, 10)
    print(isinstance(b2, Monster))
    print(isinstance(c4, Monster))

    a.print()
    c1.print()
    b2.print()
    b3.print()
    c4.print()
    print(a.hp)
    print(c1.hp)
    print(b3.ilość_gitar)
    print(b4.ilość_gitar)
    print(c4.ilość_gitar)
    c4.print()
    print(JADOWITE_DZIKI_Z_HODOWLI.mro())
    print(c4.__class__.__name__)
