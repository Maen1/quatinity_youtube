
movies = [
        {"title": "The Shawshank Redemption", "rating": 9.3, "director" : "Frank Darabont"},
        {"title": "The Godfather", "rating": 9.2, "director" : "Francis Ford Coppola"},
        {"title": "The Dark Knight", "rating": 9, "director" : "Christopher Nolan"},
        {"title": "The Godfather Part II", "rating": 9 , "director" : "Francis Ford Coppola"},
        {"title": "Aladdin", "rating": 8, "director" : "Ron Clements"},
]

for movie in movies:
	if movie["director"] == "Christopher Nolan":
		print(movie["title"])