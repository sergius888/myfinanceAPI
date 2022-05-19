# create classes for geometrical forms
# triangle, square, rectangle
# all objects need to know how many lines it has and how long is each line
# they must have a method to compute the area and perimeter
import abc
import math

# public -> from anywhere
# protected -> only from class and its children (and nephews and so on), declare with _
# private -> only from the class, declare with __ in front
from abc import abstractmethod, ABC


# an abstract class is a class which cannot be instantiated
class GeometricalForm(abc.ABC):
    def __init__(self, lines: list[float]):
        self._lines = lines  # this is a protected variable
        self.__private_var = True  # this is a private variable

    def perimeter(self) -> float:  # this is a public method
        return sum(self._lines)

    @abstractmethod  # called decorator, abstract method imposes implementation on children
    def area(self) -> float:
        pass

    def __private_method(self):
        pass


class Triangle(GeometricalForm):
    def __init__(self, line1: float, line2: float, line3: float):
        super().__init__([line1, line2, line3])

    def area(self):
        sp = self.perimeter() / 2  # semiperimeter
        return math.sqrt(sp * (sp - self._lines[0]) * (sp - self._lines[1]) * (sp - self._lines[2]))


class Rectangle(GeometricalForm):
    def __init__(self, length: float, width: float):
        super().__init__([length, length, width, width])

    def area(self) -> float:
        return self._lines[0] * self._lines[2]


class Square(Rectangle):
    def __init__(self, line: float):
        super().__init__(line, line)


if __name__ == "__main__":
    t = Triangle(3, 4, 5)
    print("triangle p", t.perimeter())
    print("triangle area", t.area())
    d = Rectangle(5, 7)
    print("rectangle p", d.perimeter())
    print("rectangle area", d.area())
    s = Square(1)
    print("square p", s.perimeter())
    print("square area", s.area())

