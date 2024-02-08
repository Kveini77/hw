# hero_v2.2
class SuperHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return (f'Прозвище героя: {self.nickname} \n'
                f'Суперспособность героя: {self.superpower} \n'
                f'Здоровье героя: {self.health_points}')

    def __len__(self):
        return len(self.catchphrase)


class SuperHeroAir(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def phrase(self):
        return f"True in the True_phrase"


class SuperHeroSpace(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2
        self.fly = True


class Villain(SuperHeroAir):
    people = "monster"

    def gen_x(self):
        ...

    def crit(self):
        self.damage **= 2


hero1 = SuperHero("Iron Man", "Тони Старк", "Бронекостюм", 150, "Я - Железный Человек!")
hero2 = SuperHero("Captain America", "Стивен Роджерс", "Суперсила и щит", 180, "Для свободы!")
hero3 = SuperHero("Black Widow", "Наташа Романофф", "Мастерство боя", 100, "Один за всех, а я за одного!")

hero_air1 = SuperHeroAir("Storm", "Оруэ Манро", "Управление погодой", 100, "Будь грозой!", 50, fly=True)
hero_air2 = SuperHeroAir("Falcon", "Сэм Уилсон", "Крылья и пушки", 120, "Вверх и вперед!", 60)
hero_air3 = SuperHeroAir("Angel", "Уоррен Уоррингтон III", "Крылья и целебные способности", 90, "Будь светлым!", 70)

hero_space1 = SuperHeroSpace("Star-Lord", "Питер Квилл", "Боевые навыки и лидерство", 120, "Мы - Стражи Галактики!", 50)
hero_space2 = SuperHeroSpace("Gamora", "Гамора", "Боевые и боевые навыки", 150, "Я - убийца!", 60, fly=False)
hero_space3 = SuperHeroSpace("Rocket Raccoon", "Ракета", "Интеллект и оружие", 100, "Я - зверь!", 60, fly=False)

villain1 = Villain("Thanos", "Танос", "Бесконечные перчатки", 300, "Я - нерушимый!", 60, fly=False)
villain2 = Villain("Loki", "Локи", "Иллюзии и хитрость", 120, "Подлость - мой дар!", 60)
villain3 = Villain("Ultron", "Ультрон", "Искусственный интеллект и технологии", 250, "Я - эволюция!", 60, fly=False)

print(f"новый аргумент demage {hero_air1.damage}\n")

print(f"герой ({hero_air2.name}) у которого по умолчанию полета нету: {hero_air2.fly}")
print(f"герой ({hero_air1.name}) у которого полет есть: {hero_air1.fly}\n")

SuperHeroAir.double_health(hero_air2)

print(f"гейрой ({hero_air2.name}) у которго не было полета после использования double_health теперь полет {hero_air2.fly} а хп равно {hero_air2.health_points}\n")

print(f"фраза ({hero_air1.name}): {hero_air1.phrase()}\n")

print(f"урон {villain1.name}: {villain1.damage}\n")

villain1.crit()
print(f"крит. урон {villain1.name}: {villain1.damage}")
