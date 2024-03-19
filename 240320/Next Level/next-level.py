class Game:
    def __init__(self, user = "codetree", level = "10"):
        self.user = user
        self.level = level

string = input().split()

people = Game()
people2 = Game(string[0], string[1])

print("user " + people.user + " lv " + people.level)
print("user " + people2.user + " lv " + people2.level)