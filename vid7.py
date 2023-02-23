class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def check_coord(self, n):
        return self.MIN_COORD <= n <= self.MAX_COORD

    def set_coords(self, x, y):
        if self.check_coord(x) and self.check_coord(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y

    # вызывается при получении свойства с именем item
    def __getattribute__(self, item):
        if item == 'm':
            raise ValueError('доступ запрещен')
        else:
            print(f'__getattribute__: {item}')
            return object.__getattribute__(self, item)

    # вызывается при изменении свойства key
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('недопустимое имя атрибута')
        else:
            print(f'__setattr__: {key} {value} ')
            object.__setattr__(self, key, value)

    # вызывается при получении несуществующего свойства item
    def __getattr__(self, item):
        print('__getattr__: ' + item)

    # вызывается при удалении свойства item
    def __delattr__(self, item):
        print('__delattr__: ' + item)
        object.__delattr__(self, item)


pt = Point(2, 4)
pt1 = Point(10, 20)
print(pt.get_coords())
pt1.w = 1000
print(pt.q)
del pt.x
print(pt.__dict__)
