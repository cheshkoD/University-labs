class Rectangle:
    def __init__(self, width: float = 2, height: float = 2):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def get_perimeter(self) -> float:
        return (self.__width + self.__width) * 2

    def get_area(self) -> float:
        return self.__width * self.__height

    def __str__(self):
        return f'Rectangle <height: { self.__height }, width: { self.__width }>'


if __name__ == "__main__":
    while True:
        width = float(input("width = "))
        height = float(input("height = "))

        rectangle = Rectangle(width, height)    # новая переменная для того что-бы использовать класс Rectangle

        print(f'Perimeter_(P): { rectangle.get_perimeter() }\nArea_(S): { rectangle.get_area() }')

        break
