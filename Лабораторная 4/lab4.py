if __name__ == "__main__":
    class Blush:
        def __init__(self, brand: str, name: str, collection: str, shade: int):
            '''Класс Румяна
                Атрибуты
                --------
                brand: str
                    бренд, выпустивший румяна
                name : str
                    названия румян
                collection : str
                    коллекция, в которой выпущены румяна
                shade : int
                    номер оттенка
                Методы
                ------
                info(additional=""):
                    Печатает имя и возраст человека.
            '''
            self.name = name
            self.brand = brand
            self.collection = collection
            self.shade = shade

        def __str__(self) -> str:
            return f'Румяна "{self.brand}" "{self.name}" коллекция "{self.collection}" в оттенке "{self.shade}"'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, collection={self.collection!r}, shade={self.shade})'

        @staticmethod
        def buy(self):
            '''Метод Покупки румян'''
            print("Blush was bought")

        def apply_blush(self):
            '''Метод Нанесения румян'''
            brush = 'brush for blush'
            print("Apply blush with" + brush)


    class LiquidBlush(Blush):
        def __init__(self, brand: str, name: str, collection: str, shade: int, volume: float, texture: str):
            '''Класс Жидкие румяна
                Атрибуты
                --------
                volume: str
                    объем жидких румян

                texture:
                    текстура румян

                Методы
                ------
                info(additional=""):
                Печатает имя и возраст человека.
            '''
            super().__init__(brand, name, collection, shade)
            self.volume = volume
            self.texture = texture
        # Перегрузим только метод __repr__, т.к. у жидких румян появились новые атрибуты,
        # но выводить для пользователя мы их не будем

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, collection={self.collection!r}, shade={self.shade}, ' \
                   f'volume={self.volume}, texture={self.texture}) '

        #метод buy унаследуем от родительского класса

        def apply_blush(self):
            '''Метод Нанесения румян
                перегрузим метод родительского класса, т.к. для каждого типа румян нужна особая кситочка
            '''
            brush = 'brush for blush liquid'
            print("Apply blush with" + brush)
    pass
