ЛОГ "ООП ДЛЯ ПОЛНЫХ КОЧЕГАРОВ"


140804-0216 == Добавлен скрипт *КлассTrap1_140801-0323.py*. Это - трапециевидное распределение на python 2.7.
Класс формирует n=1..oo значений, распределённых по трапециевидному закону.

140802-1810 == Что тут скажешь? Пока я не написал скрипт про рыцарей Круглого Стола, 
я никак не мог взят в толк, что синтаксически,
класс - это функция, 
self - это обращение этой функции к собственному имени, 
атрибуты - это "свойства", а 
методы - это "умения".


*testClass_140802-1745.py* Выдаёт на выход что-то типа:

>>>

Round 1 !!!
Sir Lancelot    strength = 1.0 health = 1.0
Sir Robin       strength = 0.5 health = 0.5
Sir Galahad     strength = 0.3 health = 0.7
Sir Other       strength = 0.5 health = 0.5
Sir Lancelot attacks Sir Robin:
Sir Robin's health is 0
Oh, yeah! Sir Robin is defeated!

Round 2 !!!
Sir Lancelot    strength = 1.0 health = 1.0
Sir Galahad     strength = 0.3 health = 0.7
Sir Other       strength = 0.5 health = 0.5
Sir Other attacks Sir Galahad:
Sir Galahad's health is 0.45

Round 3 !!!
Sir Lancelot    strength = 1.0 health = 1.0
Sir Galahad     strength = 0.3 health = 0.45
Sir Other       strength = 0.5 health = 0.5
Sir Other attacks Sir Lancelot:
Sir Lancelot's health is 0.75

Round 4 !!!
Sir Lancelot    strength = 1.0 health = 0.75
Sir Galahad     strength = 0.3 health = 0.45
Sir Other       strength = 0.5 health = 0.5
Sir Lancelot attacks Sir Galahad:
Sir Galahad's health is 0
Oh, yeah! Sir Galahad is defeated!

Round 5 !!!
Sir Lancelot    strength = 1.0 health = 0.75
Sir Other       strength = 0.5 health = 0.5
Sir Lancelot attacks Sir Other:
Sir Other's health is 0
Oh, yeah! Sir Other is defeated!

Sir Lancelot is winer! Let's drink a lot of bear!
More bear!!!
