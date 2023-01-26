## Python Sneak Peek
A short overview of python( variables, conditionals, loops  and dictionaries)

### Variables 
Python is a dynamically typed language; which means that we don't need to specify (declare) the variable type such as numbers (int, float or  double),  text types(string, char) or boolean (True, False)

Why do we need variable to begin with ?
the shor answer is to store value in it wether it's coming from a you as a programmer, or user or later own retrving it from a database

Try some examples;
```python

# Declare variables  

greeting = "Hello"
name= "John Doe"

# Different ways of printing with the same output

print(greeting, name)
print(greeting + " "+ name)


# working with different types of varibles
name = "John Doe"
age = 32
single = True

print("Name: ",name, ", Age:", age, ", Singe:", single)

print(f"Name: {name}, Age: {age}, Sinlge: {single}")

```

## Conditionals
telling the program what to do if have a certian statemts such as priting output or changing a variable value.

```python
name = "John Doe"
age = 32
single = True

# if John is single print happy, else print miserable

if single:
	print("Happy")
else:
	print("Miserable")
```

if statment with numbers 

```python
name = "John Doe"
age = 32
single = True

# compare wiht numbers we can use ==, >, <, >=, <= or !=

if age <= 32 :
	print("Cool it's 2^4")
else:
	print("Nah")

````

```python 
movie = "La la land"
rating = 7
watched = True 

# compare wiht numbers we can use ==, >, <, >=, <= or !=
# combine to conditions (and, or)

if rating >= 6 and not watched:
	print("You should watch it")
elif rating >= 6 and  watched:
	print("Already seen it")
else:
	print("It sucks")
````


## List and Loops 
Think of list as a box that contains many items 

```python 
# List (array)

movies = ["La la land", "Iron Man", "Avatar"]
ratings = [7, 8, 5]
watched = [True, False, True] 

# access value by index
# starts from zero

print(movies[1])

# using loops to go through array

for movie in movies:
	print(movie)


# or we can go by index
for i in range(len(movies)):
	print(movies[i], ratings[i], watched[i])

# using if statement with for loop

for i in range(len(movies)):
	if not watched[i]:
		print(movies[i])

````

## Dictionary 

```python
# dictionary 
# key:value pair
# movie as object(title, rating, status ...)

movie = { 
		"title" : "La la land",
		"rating": 7,
		"watched": True 
}

print(movie)
print(movie["title"])
````

```python
movies = [
        {"title": "The Shawshank Redemption", "rating": 9.3, "director" : "Frank Darabont"},
        {"title": "The Godfather", "rating": 9.2, "director" : "Francis Ford Coppola"},
        {"title": "The Dark Knight", "rating": 9, "director" : "Christopher Nolan"},
        {"title": "The Godfather Part II", "rating": 9 , "director" : "Francis Ford Coppola"},
        {"title": "Aladdin", "rating": 8, "director" : "Ron Clements"},
]
````

