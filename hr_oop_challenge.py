"""OOP CHallenge hackerrank."""
# Implement the Animal superclass here

# Copy your Animal class here and modify it to automatically count population
# Hint: Modify the initializer method to count the number of animals created
class Animal(object):
    # A variable to count population
    population = 0

    # Implement the populationCount class method here
    @classmethod
    def populationCount(cls):
        return cls.population

    def __init__(self, name):
        self.favoriteFood = "meat"
        self.name = name
        Animal.population += 1

    def sleep(self):
        print(self.name + " sleeps for 8 hours")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)


# Implement the Tiger class here as a subclass of Animal
# Hint: Implement the initializer method only
class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "meat"


# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "fish"


    def sleep(self):
        print(self.name + " hibernates for 4 months")

# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "marshmallows"


    def sleep(self):
        print(self.name + " sleeps in a cloud")


# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "leaves"

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)
        else:
            print("YUCK! " + self.name + " spits out " + food)


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "pollen"

    def sleep(self):
        print(self.name + " never sleeps")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)
        else:
            print("YUCK! " + self.name + " spits out " + food)


# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        print(self.name + " is feeding " + food + " to " + str(len(animals))
              + " animals of " + str(Animal.populationCount())
              + " total animals")
        for animal in animals:
            animal.eat(food)
            animal.sleep()
