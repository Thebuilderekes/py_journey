# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name


# def get_name(name):
#    greeting_message = f"hello {name}"
#    unauthorized_message = "this user is unauthorized"
#         print(greeting_message) if name == "Ekeopre" else print("unauthorized_message")
#
# get_name("Ekeopre")
#
# def collect_list(list_name):
#    for item in list_name:
#            print(item, "employees") if item > 1 else print(item, "employees")
#
#
# collect_list([1,2,3,4,5])

# functions can return a value
# def get_promotion(employee_level):
#    if employee_level < 8:
#        return "This employee will get a promotion"
#    else:
#        return "This employee will not get promoted"
#
# will_promote = get_promotion(10)
#
# print(will_promote)


def get_promotion(employee_level, name):
    if employee_level < 8:
        return f"{name} will get a promotion"
    return "This employee will not get promoted"


will_promote = get_promotion(4, "david")

print(will_promote)
