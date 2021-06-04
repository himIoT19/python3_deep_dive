class Rectangle:
    def __init__(self, width, height):  # 'self' is instance/object created itself. we call it any thing other than 'self', eg: 'mine', etc.
        self.width = width
        self.height = height
        # self._width = width
        # self._height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    # def to_string(self):
    #     return f"Rectangle: width={self.width}, height={self.height}"

    # def get_width(self):
    #     return self._width

    # def set_width(self, width):
    #     if width <= 0:
    #         raise ValueError("Width must be positive")
    #     else:
    #         self._width = width

    @property  # getter
    def width(self):
        return self._width

    @width.setter  # setter
    def width(self, width):
        if width < 0:
            raise ValueError("width must be positive")
        else:
            self._width = width

    # def get_height(self):
    #     return self._height

    # def set_height(self, height):
    #     if height <= 0:
    #         raise ValueError("Width must be positive")
    #     else:
    #         self._height = height

    @property  # getter
    def height(self):
        return self._height

    @height.setter  # setter
    def height(self, height):
        if height < 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
            # return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            if self.area() < other.area():
                return True
        else:
            return False


# created instance of class
r1 = Rectangle(width=10, height=20)

# get rectangle area
area = r1.area()
print(f"Area: {area}")

# get rectangle perimeter
perimeter = r1.perimeter()
print(f"Perimeter: {perimeter}")

# String of object 'r1'
print(str(r1))
# Id of object 'r1'
print(hex(id(r1)))

# using to_string
# print(r1.to_string())

# Create another rectangle instance
r2 = Rectangle(width=10, height=20)

# check for equality
print(r1 == r2)
print(r1 is r2)
print(f"{id(r1)}\n{id(r2)}")

# check
print(r1 == 100)

# rectangle 3 object
r3 = Rectangle(12, 25)

print(r1 < r3)
print(r3 > r2)

# Get and set height/width
r1.width = 100
print(r1)

# Check
r4 = Rectangle(width=-100, height=-20)
