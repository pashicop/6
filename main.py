class Animal():
    name = ''
    voice = ''
    type = ''
    weight = 0
    def __init__(self, name, weight = 0):
        self.name = name
        self.weight = weight
        list_an.append(self)
        return

    def cry(self):
        print(self.voice)
        return

    def eat(self,):
        self.weight += 1
        return

    # def get_inst(self):
    # def get_instances(cls):
    #     for inst_ref in cls.__refs__[cls]
    #         inst = inst_ref()
    #         if inst is not None:
    #             yield inst


class Artiodactyl(Animal):
    pass

class Cow(Artiodactyl):
    type = "Корова"
    voice = "Muuu"
    milk = 0

    def get_milk(self):
        self.milk += 0.3
        self.weight -= 0.3

class Goat(Artiodactyl):
    type = "Коза"
    voice = "Бееееее"
    milk = 0

    def get_milk(self):
        self.milk += 0.2
        self.weight -= 0.2

class Sheep(Artiodactyl):
    type = "Овечка"
    voice = "Меееее"
    wool = 0
    def cut(self):
        self.wool += 0.2
        self.weight -= 0.2


class Bird(Animal):
    egg = 0
    def push_egg(self):
        self.egg += 1
        self.weight -= 0.05
        return

    def eat(self,):
        self.weight += 0.2


class Goose(Bird):
    voice = "Ga-Ga"
    type = "Гусь"


class Chicken(Bird):
    voice = "Ко-Ко-Ко"
    type = "Курица"

    def push_egg(self):
        self.egg += 2
        self.weight -= 0.1
        return


class Duck(Bird):
    voice = "Кря-Кря"
    type = "Утка"

def get_birth():
    global list_an
    list_an = []
    Goose1 = Goose('Серый', 5)
    print(Goose1.type, Goose1.name)
    Goose1.cry()
    Goose2 = Goose('Белый', 5.5)
    print(Goose2.type, Goose2.name)
    Goose2.cry()
    Cow1 = Cow('Манька', 300)
    print(Cow1.type, Cow1.name)
    Cow1.cry()
    Duck1 = Duck("Кряква", 4)
    print(Duck1.type, Duck1.name)
    Duck1.cry()
    Chicken1 = Chicken("Ко-Ко", 3)
    print(Chicken1.type, Chicken1.name)
    Chicken1.cry()
    Chicken2 = Chicken("Кукареку", 2)
    print(Chicken2.type, Chicken2.name)
    Chicken2.cry()
    Sheep1 = Sheep("Барашек", 50)
    print(Sheep1.type, Sheep1.name)
    Sheep1.cry()
    Sheep2 = Sheep("Кудрявый", 55)
    print(Sheep2.type, Sheep2.name)
    Sheep2.cry()
    Goat1 = Goat("Рога", 70)
    print(Goat1.type, Goat1.name)
    Goat1.cry()
    Goat2 = Goat("Копыта", 75)
    print(Goat2.type, Goat2.name)
    Goat2.cry()
    # Eat
    print(Goose1.weight)
    print(Goose2.weight)
    Goose1.eat()
    Goose1.eat()
    print(Goose1.weight)
    print(Goose2.weight)
    print(Cow1.weight)
    Cow1.eat()
    Cow1.eat()
    print(Cow1.weight)
    Cow1.get_milk()
    print(Cow1.weight)
    Cow1.get_milk()
    print(Cow1.weight)
    print(Cow1.milk)
    print(Goat1.weight)
    Goat1.get_milk()
    Goat1.get_milk()
    print(Goat1.weight)
    Goat1.eat()
    print(Goat1.weight)
    print(Goat2.milk)
    print(Goat2.weight)
    print(Sheep1.weight)
    Sheep1.cut()
    print(Sheep1.weight)
    Sheep1.cut()
    print(Sheep1.weight)
    print(Sheep1.wool)
    print(Chicken1.weight)
    Chicken1.push_egg()
    print(Chicken1.weight)
    print(Chicken1.egg)
    Chicken1.push_egg()
    print(Chicken1.weight)
    print(Chicken1.egg)
    print(Duck1.weight)
    Duck1.push_egg()
    print(Duck1.weight)
    print(Duck1.egg)
    Duck1.push_egg()
    print(Duck1.weight)
    print(Duck1.egg)
    print()
    print(list_an)
    sum_weight = 0
    max_weight = 0
    max_weight_animal = ''
    for animal in list_an:
        # print(Animal.weight)
        sum_weight += animal.weight
        if max_weight < animal.weight:
            max_weight = animal.weight
            max_weight_animal = animal.type
        # print("{:.2f}".format(sum_weight))
    print("{:.2f}".format(sum_weight))
    print(f'Самое тяжёлое – {max_weight_animal}, {max_weight}')
    return


if __name__ == '__main__':
    get_birth()