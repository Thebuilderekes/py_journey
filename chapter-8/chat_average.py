users = {}
users["Kim"] = {
    "email": "kim@oreilly.com",
    "gender": "f",
    "age": 27,
    "friends": ["Jonah", "Josh"],
}
users["John"] = {
    "email": "john@abc.com",
    "gender": "m",
    "age": 24,
    "friends": ["Kim", "Josh"],
}
users["Josh"] = {
    "email": "josh@wickedlysmart.com",
    "gender": "m",
    "age": 32,
    "friends": ["Kim"],
}


def average_age(user):
    total_age = 0
    count = 0
    for friend in user["friends"]:
        if friend in users:
            total_age += users[friend]["age"]
            count += 1
    if count == 0:
        return 0  # or None, depending on how you want to handle no friends
    return total_age / count


# Example usage:
print(
    average_age(users["Kim"])
)  # Should average Jonah (not in users, skip) and Josh (32)
print(average_age(users["Josh"]))  # Should average Kim (27)
