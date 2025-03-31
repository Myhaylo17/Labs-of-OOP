class Animal:
    def __init__(self, name, food):
        self.__name = name  # Закритий атрибут
        self.__food = food  # Закритий атрибут

    def make_sound(self):
        raise NotImplementedError("Subclasses must contain make_sound method")

    def describe(self):
        return f"This is a {self.__class__.__name__} named {self.__name}."

    def eating(self):
        return f"The {self.__class__.__name__} named {self.__name} likes eating {self.__food}."

    # Геттери
    def get_name(self):
        return self.__name

    def get_food(self):
        return self.__food

    # Сеттери
    def set_name(self, new_name):
        self.__name = new_name

    def set_food(self, new_food):
        self.__food = new_food


class Dog(Animal):
    def make_sound(self):
        return "GAV!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Parrot(Animal):
    def make_sound(self):
        return "Cir Cir"


# Створення колекції об'єктів
animals = [
    Dog("Rex", "bone"),
    Cat("Murchuk", "fish"),
    Parrot("Kesha", "seed")
]

# Проходження по всіх елементах колекції і виклик абстрактного методу
for animal in animals:
    print(animal.describe())
    print(animal.make_sound())
    print(animal.eating())
    print()

# Взаємодія з атрибутами через сеттери
print("Changing dog's name to Max...")
animals[0].set_name("Max")
print(animals[0].describe())

print()
print("Changing cat`s food on milk")
animals[1].set_food("Milk")
print(animals[1].eating())
