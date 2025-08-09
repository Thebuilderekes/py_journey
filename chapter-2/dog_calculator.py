# set dog age in human_years 
# ask for dog name using input
# store dog name in variable 
# ask for dog age using input
# store dog age in variable 
# multiply input variable by multiply by human_years
# print "your dog_name is dog_age years old"

human_years = 7
check_dog_name = "what is your dog's name?"
check_dog_age = "how old is your dog?"
dog_name = input(check_dog_name) 
age = int(input(check_dog_age))

if int(age) > 0:
    age = age * human_years 
    print("your dog " + dog_name + " is " + str(age) + " years old")
