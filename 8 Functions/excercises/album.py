def make_album(first_name, album_title, number_tracks="unknown"):
    """makes a dictionary with artist information"""
    artist_album = {
        "First Name: ": first_name.title(),
        "Album Title: ": album_title.title()
    }
    if number_tracks:
        artist_album["Number of Tracks: "] = str(number_tracks)
    return artist_album


artist_one = make_album("james", "brown", "12")
artist_two = make_album("jimi", "hendrix")
artist_three = make_album("bon", "iver", "8")

print(artist_one)
print(artist_two)
print(artist_three)


while True:
    print("\nWhat album are you thinking of? ")
    print("type q to quit at anytime")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    album_info = make_album(f_name, l_name)
    print(album_info)
