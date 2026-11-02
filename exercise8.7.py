def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if num_songs is not None:
        album["num_songs"] = num_songs

    return album


album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Adele", "25")
album3 = make_album("Ed Sheeran", "Divide")

print(album1)
print(album2)
print(album3)

album4 = make_album("Taylor Swift", "Midnights", 13)
print(album4)