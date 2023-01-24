movies = [
	{"title": "The Shawshank Redemption", "rating": 9.3, "director" : "Frank Darabont"},
	{"title": "The Godfather", "rating": 9.2, "director" : "Francis Ford Coppola"},
	{"title": "The Dark Knight", "rating": 9, "director" : "Christopher Nolan"},
	{"title": "The Godfather Part II", "rating": 9 , "director" : "Francis Ford Coppola"},
	{"title": "Aladdin", "rating": 8, "director" : "Ron Clements"},
]

# functions or methods
def filter(dct, rating, director):
	print("From the function")
	for movie in dct:
		if movie["rating"] == rating and movie["director"] == "Christopher Nolan" :  # > < >= <= ==
			print(movie["title"])

filter(movies, 8, )

	
