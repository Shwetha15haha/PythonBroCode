# class Musics:
#     def __init__(self, name, singer, year):
#         self.name = name
#         self.singer = singer
#         self.year = year
#
#     def details(self):
#         print(f"{self.singer} is the singer of {self.name}. It was released in {self.year}.")
#
#
# musicA = Musics("ZaraZara", "Bombay Jayashri", 2001)
# musicB = Musics("CalmDown", "Rema", 2022)
#
# print(musicA.name)
# print(musicB.singer)
# musicB.details()

class Pokeman:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

pokeman1 = Pokeman(name='Skylie', attack=20)
pokeman2 = Pokeman(name='Pikachu', attack=29)
print(pokeman1.name)
print(pokeman2.name)
# print(pokeman1.attack)
print(pokeman2.attack)

pokeman1.attack = 28

print(pokeman1.attack)

# pokeman1 = Pokeman()
# print(type(pokeman1))
#
# print(dir(pokeman1))
# print(pokeman1)








