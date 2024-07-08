# import the turtle module for drawing turtle graphics
import turtle
# import the random module
import random

# set the background color to black
turtle.bgcolor('black')
# create a new turtle object named t
t = turtle.Turtle()
# set the turtle speed to the fastest 
t.speed('fastest')

# define a list named colors containing one color, 'red'. Oh, there was only red in colors list, and then I iterated. Why would the result show different colors then????
colors = ['red'] 

# iterate 399 times
for _ in range (399):
    # generate a random RGB color
    random_color = (random.random(), random.random(), random.random())  
    # the randomly generated color is added to the 'colors' list. Ahhh, is this why the result show different colored lines?
    colors.append(random_color)

# iterate 400 times, from 1 to 400 
for number in range (1, 401):
    # move the turtle 't' forward by 'number' units
    t.forward(number)
    # turn the turtle 't' to the right by 89 degrees 
    t.right(89)
    # set the pen color to the color at index 'number' in the 'colors' list
    t.pencolor(colors[number])

# finish the drawing
turtle.done()