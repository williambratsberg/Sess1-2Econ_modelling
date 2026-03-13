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

    def __repr__(self):
        """
        String representation multiple of multiple Points at the same time.
        :return: list of points in string format.
        """
        return self.__str__()

    def distance_origin(self):
        """
        Calculate the distance between point and origin.
        :return: float, distance between point and origin.
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self, point):
        """
        Calculate the distance between current point and another point.
        :param point: the other point to calculate the distance to.
        :return: float, distance between current point and another point.
        """
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __lt__(self, other):
        """
        Returns True if self is less than the other point.
        :param other: The other point to compare against
        :return: True or False
        """
        return self.distance_origin() < other.distance_origin()
p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1)
print(p1, p2)
print(f"{p2} distance to origin is {p2.distance_origin()}")
p3 = Point(12, 5)
print(f"{p3} distance to origin is {p3.distance_origin()}")
p1 = Point(6, 10)
p2 = Point(6, 15)
print(f"distance between {p1} and {p2} is {p1.distance_to(p2)}")
p4 = Point(1, 1)
points = [p1, p2, p3, p4, Point(15, 6)] #list of points, you can add a new point without defining outside the list, (just define inside the list)
print(points)
points.sort()
print(points)