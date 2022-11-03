# creating pong game 
# https://www.geeksforgeeks.org/create-pong-game-using-python-turtle/



# imported the certain library needed 
import turtle
from xml.sax.handler import all_properties 


# settings 
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("black")
sc.setup(width= 800, height = 800)


# creating the left paddle 
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("red")
left_pad.shapesize(stretch_wid=10, stretch_len=4)
left_pad.penup()
left_pad.goto(-400, 0)
# creating the left paddle 
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("red")
right_pad.shapesize(stretch_wid=10, stretch_len=4)
right_pad.penup()
right_pad.goto(400, 0)
# creating the shape of the ball 
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# setting the score
left_player = 0 
right_player = 0 
# sets the image of the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0", align="center", font=("TIMES NEW ROMAN", 25, "normal"))

# sets the ability to move paddle vertically
def paddleaup():
    y = left_pad.ycor()
    y += 35
    left_pad.sety(y)
def paddleadown():
    y = left_pad.ycor()
    y -= 35
    left_pad.sety(y)
def paddlebup():
    y = right_pad.ycor()
    y += 35
    right_pad.sety(y)
def paddlebdown():
    y = right_pad.ycor()
    y -= 35
    right_pad.sety(y)
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# true statement...
while True:
    sc.update()
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
# check borders 
    if hit_ball.ycor() > 300:
        hit_ball.sety(300)
        hit_ball.dy *= -1
    if hit_ball.ycor() < -300:
        hit_ball.sety(-300)
        hit_ball.dy *= -1
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center",font=("TIMES NEW ROMAN", 24, "normal"))
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center",font=("TIMES NEW ROMAN", 24, "normal"))
# Paddle ball collision 
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and hit_ball.ycor() > right_pad.ycor()-40): 
        hit_ball.setx(360)
        hit_ball.dx*=-1 
    if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+40 and hit_ball.ycor()>left_pad.ycor()-40):
        hit_ball.setx(-360)
        hit_ball.dx*=-1
    
