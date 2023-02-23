class Point:
    color = 'red'
    circle = 2


a = Point()
b = Point()
с = Point()

# Получение атрибута
print(getattr(Point, 'color'))
print(getattr(a, 'color'))
print(getattr(b, 'circle'))
print(getattr(b, 'radius', 'haven\'t attr'))

print('------------------------------------')

# Проверка наличия атрибута
print(hasattr(Point, 'color'))
print(hasattr(a, 'color'))
print(hasattr(a, 'radius'))

print('------------------------------------')

# Задает значение атрибута, если атрибута нет, то он создается
setattr(Point, 'color', 'green')
setattr(a, 'color', 'black')
setattr(a, 'radius', 3)

print('------------------------------------')

# Удаляет атрибут
delattr(a, 'radius')

print('------------------------------------')

print(Point.__doc__)
print(Point.__dict__)
print(a.__dict__)
print(b.__dict__)
