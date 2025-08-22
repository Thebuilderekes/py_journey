users = {}
users["Kim"] = {
    "email": "kim@oreilly.com",
    "gender": "f",
    "age": 27,
    "friends": ["John", "Josh"],
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

# Copied selected text to selection primary: Now that we know how we’re going to store our users on the Anti-Social Network, it’s time to write a little code. Let’s create a function we might need for the startup, called average_age, that takes a name and returns the average age of that user’s friends.

# We’re letting you tackle this on your own—after all, it is Chapter 8—although don’t forget to write some some pseudocode or do similar planning, as it goes a long ways toward writing correct code the first time.


def get_average_age(users_item, username):

    def get_friends_age_sum(username):
        sum_of_ages = 0
        for name in users_item:
            if name in users_item[username]["friends"]:
                sum_of_ages = sum_of_ages + users_item[name]["age"]
        return sum_of_ages

    age_sum = get_friends_age_sum(username)
    average_age = age_sum / len(users_item[username]["friends"])
    return average_age


age_average = get_average_age(users, "John")
print(age_average)


# average_age = sum_of_ages_of_friends/length of the friends_list
# return average_age
