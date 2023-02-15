class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def __del__(self):
        print('Удаление экземпляра:' + str(self))


pt = Point(2, 4)
print(pt.__dict__)
