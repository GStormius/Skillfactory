class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rectangle(self):
        return 'Rectangle({width}, {height})'.format(width=self.width, height=self.height)


new_rectangle = Rectangle(5, 10)
print(new_rectangle.get_rectangle())