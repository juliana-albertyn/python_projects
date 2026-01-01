"""
Module: build-a-polygon-area-calculator
Purpose: Explore OO and inheritance

Defines Rectangle and Square classes with methods for geometric calculations and ASCII rendering.
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-01"

from math import sqrt, floor


class Rectangle:
    """
    Represents a rectangle shape.

    Provides methods to modify dimensions and compute geometric properties such as area,
    perimeter, diagonal length, and ASCII art rendering.

    Attributes:
    width (float) : Width.
    height (float) : Height.
    """

    def __init__(self, width: float, height: float) -> None:
        """Initialise a new Rectangle instance

        Args:
        width (float): The initial width.
        height (float): The initial height.
        """
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """Return a str representation.

        Returns:
        str: A str with the class name, width, and height
        """
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: float) -> None:
        """Sets the width.

        Args:
        width (float): New value for width.
        """
        self.width = width

    def set_height(self, height: float) -> None:
        """Sets the height.

        Args:
        height (float): New value for height.
        """
        self.height = height

    def get_area(self) -> float:
        """Return the area.

        Returns:
        float: The area.
        """
        return self.width * self.height

    def get_perimeter(self) -> float:
        """Returns the perimeter.

        Returns:
        float: The perimeter.
        """
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        """Returns the diagonal.

        Returns:
        float: The diagonal.
        """
        return sqrt(self.width**2 + self.height**2)

    def get_picture(self) -> str:
        """Return an ASCII art representation of the rectangle using '*' characters.
        Returns:
        str: The ASCII drawing or "Too big for picture." if the dimensions exceed 50.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        result = ""
        for h in range(1, floor(self.height) + 1):
            result += f'{"*" * floor(self.width)}\n'
        return result

    def get_amount_inside(self, shape: "Rectangle") -> int:
        """Returns the number of times a shape fits into the Rectangle.

        Args:
        shape (Rectangle): An instance of Rectangle.

        Returns:
        int: The number of times the passed in shape fits into the Rectangle.
        """
        if shape.width > self.width or shape.height > self.height:
            return 0
        across = floor(self.width / shape.width)
        down = floor(self.height / shape.height)
        return across * down


class Square(Rectangle):
    """
    A rectangle with all sides equal.

    Inherits from Rectangle and overrides setters to ensure width and height remain equal.
    """

    def __init__(self, side: float) -> None:
        """Initialise a new Square instance

        Args:
        side (float): Initial height and width.
        """
        super().__init__(side, side)

    def __str__(self) -> str:
        """Returns a str representation of the instance.
        Returns:
        str: Class name and width.
        """
        return f"Square(side={self.width})"

    def set_width(self, width: float) -> None:
        """Sets the width and height.

        Args:
        width (float): new width and height.
        """
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height: float) -> None:
        """Sets the width and height.

        Args:
        height (float): new width and height.
        """
        super().set_width(height)
        super().set_height(height)

    def set_side(self, side: float) -> None:
        """Sets the width and height.

        Args:
        side (float): new width and height.
        """
        super().set_width(side)
        super().set_height(side)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
