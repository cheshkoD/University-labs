class Rational:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        self.is_optimized = False

        self.optimize_numbers()

    def optimize_numbers(self):
        def optimize(number):
            if number % 2 == 0:
                return 2
            elif number % 3 == 0:
                return 3
            elif number % 5 == 0:
                return 5
            return False

        if (optimize(self.a) and optimize(self.b)) and (optimize(self.a) == optimize(self.b)):
            self.a = self.a / optimize(self.a)
            self.b = self.b / optimize(self.b)

            self.optimize_numbers()
        else:
            self.is_optimized = True

    def str(self, print_as_float = True):
        if print_as_float:
            return self.a / self.b
        else:
            return f'{ self.a }/{ self.b }'

    def __str__(self):
        return f'Rational <a: { self.a }, b: { self.b }, is_optimized: { self.is_optimized }, float: { self.str() }>'


if __name__ == "__main__":
    while True:
        a = float(input("a = "))
        b = float(input("b = "))

        rational = Rational(a, b)

        print(f'Print as float: { rational.str() }\nPrint as a/b: { rational.str(False) }')

        break