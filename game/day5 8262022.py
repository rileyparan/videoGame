# https://docs.python.org/3/library/turtle.html

from turtle import * #turtle enables to create pictures/shapes 

from random import randint #random float number [0.1-1]
myColors = ['red,' 'green,' 'blue,' 'purple,'] #draws on the image with the specific colors presented 
def rand_color (): #controls the luminosity of the color 
    return myColors [randint (0,2)]

def rand_num(x,y,z):
    return(randint(x,y)) #randomizes the amount of colors inputed 

color('red', 'yellow') #add mores colors 
begin_fill()
# comments go here...
while True: #below controls/defines shape/size and the loop
        forward (randint(1,10))
        left (170)
        if abs(pos()) < 1:
            break 
end_fill ()
done()
