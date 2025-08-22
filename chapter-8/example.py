"""testing out dictionary formations using movies list and movies dictionary"""

# movies = []
# movie = {}
# movie["name"] = "Forbidden Planet"
# movie["year"] = 1957
# movie["rating"] = "*****"
# movie["year"] = 1956
# movies.append(movie)
# movie2 = {"name": "I Was a Teenage Werewolf", "year": 1957, "rating": "****"}
# movie2["rating"] = "***"
# movies.append(movie2)
# movies.append(
#    {"name": "Viking Women and the Sea Serpent", "year": 1957, "rating": "**"}
# )
# movies.append({"name": "Vertigo", "year": 1958, "rating": "*****"})
# print("all movies", movies)
# print("Head First Movie Recommendations")
# print("--------------------------------")
# print("movies with ratings of 4 stars or greater")
#
# for movie in movies:
#    if len(movie["rating"]) >= 4:
# print(movie["name"], "(" + movie["rating"] + ")", movie["year"])
# Creating a dictionary
person = {"name": "Alice", "age": 30, "is_active": True}

# Accessing values
print(person["name"])  # Alice

# Adding/Updating entries
person["email"] = "alice@example.com"

# Checking if a key exists
if "age" in person:
    print(person["age"])

    print("----------")
# Iterating
for key, value in person.items():
    print(f"{key}: {value}")
