# Implement a class called RegularPolygon with the following:

# 1. A constructor method that initializes two instance properties: the number
#    of sides for the polygon and the length of each side. If the number of
#    sides is less than 3, raise an Exception with the message "A polygon must
#    have at least 3 sides."

# 2. A class variable called type set to an inital value of "Polygon"

# 3. An instance method called identify_polygon that identifies the type of a
#    polygon based on its number of sides. This method should set the type class
#    variable for this instance to the identified type based on the logic in the
#    starter repl.

# 4. A class method called polygon_factory that is a factory function for
#    creating instances of the class. This method should take a list of tuples
#    as an argument, where each tuple contains the (num_sides, length) for each
#    RegularPolygon instance to be created. The method should return a list of
#    all the class instances created.

# 5. A static method called get_perimeter that calculates and returns the
#    perimeter of a polygon. This method should take an instance of the
#    `RegularPolygon` class and return the calculated perimeter. (The perimeter
#    of a regular polygon is the product of the number of sides multiplied by
#    the length of each side.)

# Polygons
# 3 sides - Triangle
# 4 sides - Quadrilateral
# 5 sides - Pentagon
# 6 sides - Hexagon
# 7 sides - Heptagon
# 8 sides - Octagon
# 9 sides - Nonagon
# 10 sides - Decagon
# Greater than 10 sides - Polygon with n sides

# Write your class here.
class RegularPolygon:
    type = "Polygon"

    def __init__(self, num_sides, length):
        if num_sides < 3:
            raise Exception("A polygon must have at least 3 sides")
        self._num_sides = num_sides
        self._length = length

    @property
    def num_sides(self):
        return self._num_sides

    @property
    def length(self):
        return self._length

    def identify_polygon(self):
        if self._num_sides == 3:
            self.type = "Triangle"
        elif self._num_sides == 4:
            self.type = "Quadrilateral"
        elif self._num_sides == 5:
            self.type = "Pentagon"
        elif self._num_sides == 6:
            self.type = "Hexagon"
        elif self._num_sides == 7:
            self.type = "Heptagon"
        elif self._num_sides == 8:
            self.type = "Octagon"
        elif self._num_sides == 9:
            self.type = "Nonagon"
        elif self._num_sides == 10:
            self.type = "Decagon"
        elif self._num_sides > 10:
            self.type = f"Polygon with {self._num_sides} sides"

    @classmethod
    def polygon_factory(cls, lst):
        result = []
        for tupl in lst:
            result.append(cls(tupl[0], tupl[1]))
        return result

    @staticmethod
    def get_perimeter(instance):
        return instance.num_sides * instance.length

    def __repr__(self):
        return f'<Regular Polygon object with {self._num_sides} sides of length {self._length}>'

pentagon = RegularPolygon(5, 5)
octagon = RegularPolygon(8, 10)
dodecagon = RegularPolygon(12, 1)

print(f"{pentagon.num_sides} sides of length {pentagon.length}") # 5 sides of length 5
print(f"{octagon.num_sides} sides of length {octagon.length}") # 8 sides of length 10
print(f"{dodecagon.num_sides} sides of length {dodecagon.length}") # 12 sides of length 1

pentagon.identify_polygon()
octagon.identify_polygon()
dodecagon.identify_polygon()

print(pentagon.type) # Pentagon
print(octagon.type) # Octagon
print(dodecagon.type) # Polygon with 12 sides

print(RegularPolygon.polygon_factory([(5, 5), (3, 2), (8, 10)])) # prints a list of 3 RegularPolygon objects

print(RegularPolygon.get_perimeter(pentagon)) # 25
print(RegularPolygon.get_perimeter(octagon)) # 80
print(RegularPolygon.get_perimeter(dodecagon)) # 12

try:
    not_a_polygon = RegularPolygon(2, 5) # Exception: A polygon must have at least 3 sides.
except Exception as e:
    print(f'Exception: {e}')
