def make_shirt(size="large", message="I love Python"):
    """Display the shirt size and its printed message."""
    print(f"The shirt size is {size} and the message "
          f"printed on it is '{message}'.")


make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="Keep Learning")



#part 2
def make_album(artist, title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {
        "artist": artist,
        "title": title
    }

    if num_songs is not None:
        album["num_songs"] = num_songs

    return album


album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Adele", "25")
album3 = make_album("Ed Sheeran", "Divide", 16)

print(album1)
print(album2)
print(album3)


#part 3
def make_car(manufacturer, model, **car_info):
    """Build a dictionary describing a car."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    return car_info


car = make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)

print(car)