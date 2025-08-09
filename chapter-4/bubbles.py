#check the value of current number
#assume the highest number is the first number in the list
#loop through thee numbers and check if the score is greater than the highest number
#if it is, set the value of the highest number to score
#print the highest number



scores = [200, 40, 101, 50, 30, 40, 20, 50, 60, 40, 30, 70, 90, 80]



#Solutions
# using  while loop 

#iterations = len(scores)
#i = 0
#while True:
#    if i < iterations:
#        print("buble solution" + "#",  i, "score:", scores[i]  )
#        i = i + 1
#    else:
#        break

#Using for loop - The preferable way 
# method 1 for loops using enumerate()
#for index, score in enumerate(scores):
#    bubble_string = "bubble string #" + str(index) + " has score: " + str(score)   
#    #we store the string in a variable of readability and organization else you can directly have the string as an argument to the print function using print(f"bubble string #{index} has score:  {score}")   
#    print(bubble_string)
#    #print(f"bubble string #{index} has score:  {score}")  #preferable 

# method 2 for loops using range- this is the more popular method
length = len(scores)
for i in range(length):
    print(f"bubble string #{i} has score:{scores[i]}")  #preferable 


# you can use list(range(5)) to create a list [0,1,2,3,4]
# read more about range() and the different things you can do with it


# To find the highest score:
highest_score = scores[0] #assuming the last first number to be the highest score

for index, score in enumerate(scores):
    if score > highest_score:
        highest_score = score
        highest_score_index = index(score)
        print(f"the index with the highest score is {highest_score_index}")




