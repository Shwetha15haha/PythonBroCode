class Musics:
    def __init__(self, name, singer, year):
        self.name = name
        self.singer = singer
        self.year = year

    def details(self):
        print(f"{self.singer} is the singer of {self.name}. It was released in {self.year}.")


musicA = Musics("ZaraZara", "Bombay Jayashri", 2001)
musicB = Musics("CalmDown", "Rema", 2022)

print(musicA.name)
print(musicB.singer)
musicB.details()
