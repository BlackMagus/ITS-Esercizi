def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    if num_songs:
        album['numero canzoni'] = num_songs
    return album


album_1 = make_album('Andrea', 'Album 1')
album_2 = make_album('Alessio', 'Album 2', 10)
album_3 = make_album('Gianluca', 'Album 3', 16)


print(album_1)
print(album_2)
print(album_3)