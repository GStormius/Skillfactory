from rectangle import Rectangle, Square, Circle

#  Создание двух прямоугольников и вывод результата вычисления их площади
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area_rectangle(),
      rect_2.get_area_rectangle())

#  Создание двух квадратов и вывод результата вычисления их площади
square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

#  Создание двух кругов и вывод результата вычисления их площади
circle_1 = Circle(4)
circle_2 = Circle(6)

print(format(circle_1.get_area_circle(), '.2f'),
      format(circle_2.get_area_circle(), '.2f'))

print('------------')

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print((figure.get_area_circle()))
    else:
        print(figure.get_area_rectangle())
