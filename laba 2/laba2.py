from abc import ABC, abstractmethod
import math

# Абстрактний клас Shape (Open/Closed Principle)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Клас для прямокутника (Single Responsibility)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Клас для круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Клас, відповідальний лише за виведення (Single Responsibility)
class ShapePrinter:
    def print_area(self, shape: Shape):
        print(f"Area: {shape.area():.2f}")

# Головна функція
def main():
    rectangle = Rectangle(7, 9)
    circle = Circle(5)

    printer = ShapePrinter()
    printer.print_area(rectangle)
    printer.print_area(circle)

if __name__ == "__main__":
    main()
