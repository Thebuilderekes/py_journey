def average_age(users_dict, username):
    average = 0
    friends_list_age = []
    for key, users_dict[username] in users:
        if users_dict[username][key] == "friends":
            for names in users_dict[username][key]:
                friends_list_age.append(names.age)
    for age in friends_list_age:
        sum_ages = sum_ages + age
        print("sum is", sum_ages)
        average = sum_ages/len(friends_list_age)
    return average


print("average age is :", average_age(users["Kim"]))
