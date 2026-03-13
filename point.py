class Point: # we use capital letters only for class names
    """
    Simple class to represent a point in 2D space.
    """
    def __init__(self, x, y):  # since a def is inside of a class, it is a method, (we define a class method),
        # self is always the first parameter of a class, self is the unique structure you will have each time you instantiate a new object
        """
        Constructor for Point class.
        :param x: x coordinate of point.
        :param y: y coordinate of point.
        """
        self.x = x # x is a class attribute (same with y)
        self.y = y
    def __str__(self):
        """
        String representation of Point class.
        :return: String representation of Point class.
        """
        return f"(P<{self.x},{self.y}>)" # defining how strings are represented in the point class
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point("bob", {1, 2, 3})

print(p1.x, p1.y)
print(p2.x, p2.y)
print(p3.x, p3.y)
print(p1)
print(p1, p2)