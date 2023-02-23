def read():
    return 'Данные из БД'


def read():
    return 'Данные из БД'


class DataBase:
    """
    Пример реализации класса с применением паттерна Singleton и магического метода __new__
    При реализации паттерна Singleton создается один единственный экземпляр класса, другие созданные будут
    ссылаться на этот, первый созданный, экземпляр
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data):
        print(f'Запись в БД {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', 'qwer', 88)

print(id(db), id(db2))
