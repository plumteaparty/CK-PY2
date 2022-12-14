# TODO Написать 3 класса с документацией и аннотацией типов

class Album:
    def __init__(self, title:str, artist: str, track_number: int, length:float):
        self.artist = artist #автор альбома
        self.track_number = track_number#количество треков
        self.length = length#длительность альбома
        self.title = title#название альбома
    def recording_album(self, title:str,artist: str,track_number: int, length:float):
        '''
        Функция для записи альбома
        :param title: Название альбома
        :rise TypeError: Название альбома должно быть типа str
        :param artist: Имя артиста
        :rise TypeError: Имя артиста должно быть типа str
        :param track_number: Количество песен на альбоме
        :rise TypeError: Количество песен на альбоме должно быть типа int
        :rise ValueError: Количество песен на альбоме должно быть больше 0
        :param length: Длительность альбома
        :rise TypeError: Длительность альбома должна быть типа float
        :rise ValueError: Длительность альбома должна быть больше 0
        >>> album = Album()
        >>> album.recording_album('AM', 'Arctic Monkeys', 12, 41.5)
        '''
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
        '''
        :return: Возвращает состояние альбома - альбом выпущен
        >>>album.realesing_album()
        '''
        #метод выпускает альбом
        print("Альбом выпущен")
    def promoting_album(self):
        '''
        :return: Возвращает состояние альбома - альбом продвигается
        >>>album.promoting_album()
        '''
        #метод продвигает альбом
        print("Продвижение альбома началось")


class Artist:
    # класс - карточка исполнителя на стриминговом сервисе
    def __init__(self, name: str, albums_number: int, awards_number: int, streams: int):
        '''
        конструктор класса
        :param name: Имя артиста
        :rise TypeError: Имя артиста должно быть типа str
        :param albums_number: Количество альбомов
        :rise TypeError: Количество альбомов должно быть типа int
        :rise ValueError: Количество альбомов должно быть больше 0
        :param awards_number: Выигранная премия
        :rise TypeError: Количество выигранных премий должно быть типа int
        :param streams: Количество прослушиваний на площадке
        :rise TypeError: Количество прослушиваний на площадке быть типа int
        :rise ValueError: Количество альбомов должно быть больше 0
        >>>artist = Artist('Arctic Monkeys', 7, 5, 1000000)
        '''
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
        '''
        метод записывает песню
        :param track_number: Количество записанных песен
        :rise TypeError: Количество записанных песен быть типа int
        :rise ValueError: Количество записанных песен быть больше 0
        >>>artist.track_record(1)
        '''
        if not isinstance(track_number, int):  # проверяем, что количество записанных песен типа int
            raise TypeError("Количество записанных песен должно быть типа int")  # вызываем ошибку
        if track_number < 0:
            raise ValueError("Количество записанных песен должно быть положительным числом")
        self.track_number += track_number
    def rewarded(self):
        '''
        метод получает награду
        >>>artist.rewarded()
        '''
        self.awards_number += 1



class Track:
    def __init__(self, title: str, artist: str):
        '''
        конструктор класса
        :param title: Название трека должно быть типа str
        :rise TypeError: Название трека должно быть типа str
        :param artist: Имя артиста
        :rise TypeError: Имя артиста должно быть типа str
        >>>track = Track('Do I Wanna Know?', 'Arctic Monkeys')
        '''
        if not isinstance(title, str):  # проверяем, что название трека указано правильно
            raise TypeError("Некорректное название трека")  # вызываем ошибку
        self.title = title
        if not isinstance(artist, str):  # проверяем, что имя артиста указано правильно
            raise TypeError("Некорректный испольнитель")  # вызываем ошибку
        self.artist = artist
        self.length = 0.0

    def recording_track(self, length: float):
            '''
            метод записывает песню
            :param length: Длительность трека
            :rise TypeError: Длительность трека должна быть типа float
            :rise ValueError: Длительность трека должна быть больше 0
            >>> track.recording_track(4.5)
            '''
            if not isinstance(length, float):  # проверяем, что длина трека типа float
                raise TypeError("Длина трека должна быть типа float")  # вызываем ошибку
            if length < 0:
                raise ValueError("Длина трека должна быть больше нуля")
            self.length += length

    def realesing_track(self):
        '''
        метод выпускает трек
        :return: Возращает состояние трека - выпущен
        >>> track.realesing_track()
        '''
        print("Трек выпущен")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
