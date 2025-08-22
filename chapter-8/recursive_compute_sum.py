"""Example of recursive sum of list"""


# This is a great recursive example so Keep coming to this function to check it
def recursive_compute_sum(number_list):
    if len(number_list) == 0:
        return 0
    first = number_list[0]
    rest = number_list[1:]
    print(first)
    print(rest)
    sum_list = first + recursive_compute_sum(rest)
    return sum_list


print(recursive_compute_sum([1, 2, 3]))
