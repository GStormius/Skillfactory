class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_attributes_of_rectangle(self):
        return 'Rectangle({width} {height} {area})'.format(width=self.width, height=self.height, area=self.get_area())


new_rectangle = Rectangle(5, 18)
print(new_rectangle.get_attributes_of_rectangle())
