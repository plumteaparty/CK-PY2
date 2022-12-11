# TODO Написать 3 класса с документацией и аннотацией типов

class Album:
    def __init__(self, title:str, artist: str, track_number: int, length:float):
        self.artist = artist #автор альбома
        self.track_number = track_number#количество треков
        self.length = length#длительность альбома
        self.title = title#название альбома
    def recording_album(self, title:str,artist: str,track_number: int, length:float):
        #метод записывает альбома - присваивание значений атрибутам
        if not isinstance(title, str):  # проверяем, что название альбома указано правильно
            raise TypeError("Некорректное название альбома")  # вызываем ошибку
        self.title = title
        if not isinstance(artist, str):  # проверяем, что имя артиста указано правильно
            raise TypeError("Некорректный испольнитель")  # вызываем ошибку
        self.artist = artist
        if not isinstance(track_number, int):  # проверяем, что количество треков на альбоме - целове число
            raise TypeError("Некорректное колличество треков")  # вызываем ошибку
        if track_number <= 0:
            raise ValueError("Колличетво треков на альбоме не может быть отрицательным. На альбоме должны быть треки")
        self.track_number = track_number
        if not isinstance(length, float):  # проверяем, что длительность альбома - вещественное число
            raise TypeError("Длительность альбома должно быть вещественным числом")  # вызываем ошибку
        if length <= 0:
            raise ValueError("Длительность альбома должна быть больше нуля")
        self.length = length
    def realesing_album(self):
        #метод выпускает альбом
        print("Альбом выпущен")
    def promoting_album(self):
        #метод продвигает альбом
        print("Продвижение альбома началось")


class Artist:
    # класс - карточка исполнителя на стриминговом сервисе
    def __init__(self, name: str, albums_number: int, awards_number: int, streams: int):
        if not isinstance(name, str):  # проверяем, что имя исполнителя указано правильно
            raise TypeError("Некорректное имя исполнителя")  # вызываем ошибку
            self.name = name # имя исполнителя
        if not isinstance(albums_number, int):  # проверяем, что название альбома указано правильно
            raise TypeError("Некорректное количество альбомов")  # вызываем ошибку
            self.albums_number = albums_number  # количество записанных альбомов - целое число
        if not isinstance(awards_number, int):  # проверяем, что количество полученных премий - целое число
            raise TypeError("Некорректное количество наград")  # вызываем ошибку
            self.awards_number = awards_number # количество полученных премий
        if not isinstance(streams, int):  # проверяем, что количество прослушиваний на площадке - целое число
            raise TypeError("Некорректное количество прослушиваний")  # вызываем ошибку
            self.streams = streams # количество прослушиваний на площадке
    def track_record(self, track_number: int):
        # метод записывает песню
        if not isinstance(track_number, int):  # проверяем, что количество записанных песен типа int
            raise TypeError("Количество записанных песен должно быть типа int")  # вызываем ошибку

        if track_number < 0:
            raise ValueError("Количество записанных песен должно быть положительным числом")

        self.track_number += track_number


class Track:
    def __init__(self, title: str, artist: str):
        if not isinstance(title, str):  # проверяем, что название трека указано правильно
            raise TypeError("Некорректное название трека")  # вызываем ошибку
        self.title = title
        if not isinstance(artist, str):  # проверяем, что имя артиста указано правильно
            raise TypeError("Некорректный испольнитель")  # вызываем ошибку
        self.artist = artist
        self.length = 0.0

    def recording_track(self, length: float):
            # метод записывает песню
            if not isinstance(length, float):  # проверяем, что длина трека типа float
                raise TypeError("Длина трека должна быть типа float")  # вызываем ошибку
            if length < 0:
                raise ValueError("Длина трека должна быть больше нуля")
            self.length += length

    def realesing_track(self):
        # метод выпускает трек
        print("Трек выпущен")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
