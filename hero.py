
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
                f'Суперспособность героя:{self.superpower} \n'
                f'Здоровье героя: {self.health_points} \n')
    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Bruh", "Рен Довер", "Щит оправдания", 100, "Бывает")

print(hero)
hero.double_health()
print(hero.health_points)
print(f"Длина коронной фразы героя: {len(hero)}")
