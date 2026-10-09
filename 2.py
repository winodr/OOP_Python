class Character:

    def __init__(self, name: str, health: int = 100, damage: int = 15):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        if target.health > 0:
            target.health -= self.damage
            return f'{self.name} нанёс урон {target.name} в количестве {self.damage}\nУ {target.name} осталось {target.health} хп'
        else:
            return f'{target.name} мёртв'




class Mage(Character):
    
    def __init__(self, name: str, health: int , damage: int, mana: int = 50):
        super().__init__(name, health, damage)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            if target.health > 0:
                target.health -= self.damage*2
                self.mana -= 10
                return f'{self.name} нанёс урон {target.name} в количестве {self.damage*2}\nУ {target.name} осталось {target.health} хп'
            else:
                return f'{target.name} мёртв'
        else:
            return super().attack(target)


Warrior = Character('Орк', health=20)
mage = Mage('Эльф', health=70, damage=10)
print(mage.attack(target=Warrior))