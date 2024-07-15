# 8-6 City Names

def city_country(city, country):
	return f"{city.title()}, {country.title()}"

print(city_country('Barcelona', 'Spain'))
print(city_country('berlin', 'germany'))
print(city_country('Paris', 'France'))

# 8-7 Album

def make_album(artist, album_name, num_songs = None):
	album = {
		'album_name' : album_name,
		'artist' : artist}
	if num_songs:
		album['num_songs'] = num_songs

	return album

album = make_album('coldplay', 'XY', 13)
print(album)

album = make_album('rosalia', 'motomami')
print(album)

album = make_album('manel', 'jo competeixo')
print(album)

# 8-8 User Albums 

while True:
	artist = input("Artist: ")
	if artist == 'q':
		break

	album_name = input("Album: ")
	num_songs = input("Number of songs: ")

	album = make_album(artist = artist, album_name = album_name, num_songs = num_songs)
	print(album)
