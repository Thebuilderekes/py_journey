import turtle

speedy = turtle.Turtle()
speedy.shape("turtle")
speedy.pensize(10)
speedy.color("red")


def make_move(animal):
    i = 0
    for i in range(0, 4): # runs this function 4 times
        animal.forward(100)
        animal.right(90)

# one way to refactor this code when you are 
# building individual shapes is to have one 
# function for each shape and then one main function to execute each individual shape

make_move(speedy)
