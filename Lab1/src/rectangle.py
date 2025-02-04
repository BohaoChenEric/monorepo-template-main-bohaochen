"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
class Shape:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        pass

    def set_values(self, width, height):
        self._width = width
        self._height = height
    
class Rectangle(Shape):
    def area(self):
        return self._width * self._height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(0, 0)

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())