class Album:
    GENRES = ["Hip-Hop", "Pop", "Jazz"]
    album_count = 0

    def __init__(self, genre, date):
        if self.check_genre(genre):
            self.increase_album_count()
            self.genre = genre
            self.release_date = date

    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES


album = Album("Hip-Hop", 1991)
album1 = Album("Pop", 1998)
album2 = Album("Pop", 2002)
album3 = Album("Rap", 1995)
# print(album.release_date, album.album_count)
print(Album.album_count)
