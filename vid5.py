class Vector:
    """
    Пример реализации статического метода и метода класса
    метод класса - для работы с атрибутами класса, не может работать с атрибутами экземпляра
    статический метод - независимый метод, который работает с параметрами определенными в нем
    """
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(10, 20)
print(v.get_coord())
print(v.norm2(5, 6))
print(Vector.norm2(50, 60))
