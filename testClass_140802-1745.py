# coding: utf
# python: 2.75

from __future__ import division # Деление вида "1/10"
from random import choice # Выбор случайного значения из списка

# Это полезная функция, она пригодится нам позже:
def drinkBear(*args):
    print 'More bear!!!'
    pass
    pass
    pass
# Это класс Рыцарей Круглого Стола. Рыцарь обладает свойствами (атрибутами) "имя", "легенда", "сила" и "здоровье", а ещё умением (методом), менять свой атрибут "здоровье" при ранениях. Внутри класса есть небольшая база данных по рыцарям, выдающая рыцарям те или иные свойства в зависимости от имени.
class knight:
    '''It's a knight of the Round Table.'''
    def __init__(self,name):
        self.name = name
        # Это база данных по рыцарям:
        if name == 'Sir Lancelot': 
            self.bio = "The most famous of Arthur's knights, lover of Queen Guinevere and father of Galahad."
            self.strength = 10/10
            self.health = 10/10
        elif name == 'Sir Robin': 
            self.bio = "The bravest of Arthur's knights."
            self.strength = 5/10
            self.health = 5/10
        elif name == 'Sir Galahad': 
            self.bio = "The purest of Arthur's knights."
            self.strength = 3/10
            self.health = 7/10
        else:
            self.bio = "I don't remember him, my dear children."
            self.strength = 5/10
            self.health = 5/10
    # Это умение менять свой атрибут "здоровье":
    def newHealth(self,newHea):
        if newHea < 42e-6: newHea = 0
        self.health = newHea
# Это функция, определяющая механизм удара. Здоровье того, кого бьют, уменьшается пропорционально силе того, кто ударил:
def hit(aStr,dHea):
    return dHea-aStr/2
# Это функция, описывающая атаку. Пишет, кто на кого напал, меняет здоровье свежеозвездюленного и улюлюкает:
def attack(a,d):
    print a.name, 'attacks', d.name+':'
    d.newHealth(hit(a.strength,d.health))
    print d.name+"'s health is", d.health
    if d.health <= 0: print 'Oh, yeah!', d.name, 'is defeated!'
# Это список участников побоища:
# Большая драка:
guys = [knight('Sir Lancelot'),
        knight('Sir Robin'),
        knight('Sir Galahad'),
        knight('Sir Other')]
# Небольшая (отладочная) драка:
# guys = [knight('Sir Lancelot'),
        # knight('Sir Robin')]
# А это битва! Набирается список тех, кто пока жив (если жив только один - он объявляется победителем и битва переходит в попойку). Выводится список участников раунда и их параметры. Случайным образом назначается тот кто бьёт и тот, в кого прилетает. Атака!
for i in xrange(42):
    guysInFight = []
    for guy in guys: 
        if guy.health > 0: 
            guysInFight.append(guy)
    if len(guysInFight) == 1:
        print guysInFight[0].name, "is winer! Let's drink a lot of bear!"
        drinkBear()
        break
    print 'Round', i+1, '!!!'
    for guy in guysInFight: print guy.name, '\t', 'strength =',guy.strength, 'health =', guy.health
    nums = range(len(guysInFight))
    aNum = choice(nums)
    nums.remove(aNum)
    dNum = choice(nums)
    a, d = guysInFight[aNum], guysInFight[dNum]
    attack(a,d)
    print
    
    
