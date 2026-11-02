def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if num_songs is not None:
        album["num_songs"] = num_songs

    return album


while True:
    print("Enter album information:")
    print("Enter 'q' at any time to quit.")

    artist = input("Artist name: ")

    if artist.lower() == "q":
        break

    title = input("Album title: ")

    if title.lower() == "q":
        break

    album = make_album(artist, title)

    print(album)

print("Program has ended.")