group_of_heroes = []

class Superhero:
    def __init__(self, name, age = 0, power = "n"):
        self.name = name
        self.age = age
        self.power = power

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_super_power(self, power):
        self.power = power

    def __str__(self):
        if self.power in 'f': 
            power = "Flying"
        elif self.power in 'g': 
            power = "Giant"
        elif self.power in 'h': 
            power = "Hacker"
        elif self.power in 'n': 
            power = "None"
        else:
            power = "Weakling"

        return "{} ({}): {}".format(self.name, self.age, power)

def createGroupOfHeroes():
    amount_of_heroes = input("How many heroes should there be in the group : ")
    amount_of_heroes_int = int(amount_of_heroes)

    for _ in range(amount_of_heroes_int):
        hero_name = input("Type in the hero name : ")
        hero_age = input("Type in the hero age : ")
        hero_power = input("Type in the hero power : ")
        group_of_heroes.append(Superhero(hero_name,hero_age,hero_power))

def main():
    createGroupOfHeroes()
    for i in group_of_heroes:
        print(i)

main()