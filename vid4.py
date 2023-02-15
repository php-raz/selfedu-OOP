class Point:

    def __new__(cls, *args, **kwargs):
        print('вызов функции __new__ для ' + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('вызов функции __init__ для ' + str(self))
        self.x = x
        self.y = y


pt = Point(2, 4)
print(pt)



