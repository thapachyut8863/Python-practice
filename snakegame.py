import turtle
win = turtle.Screen()
win.title("Achyut snake game")
win.bgcolor("blue")
win.setup(width=600,height=600)
win.tracer(0)

#head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

while True:
    win.update()




def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)



    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)    


    if head.direction == "right":
        x = head.xcor()
        head.sety(x + 20)



    if head.direction == "left":
        y = head.xcor()
        head.sety(x - 20)    




while True:
    win.update()
    move()




import turtle
import time
delay=0.1
while True:
    win.update()
    move()
    time.sleep(delay)    


def go_up():
    if head.direction != "down" :
        head.direction ="up"



def go_down():
    if head.direction != "up" :
        head.direction ="down"



def go_right():
    if head.direction != "left" :
        head.direction ="right" 



def go_left():
    if head.direction != "right" :
        head.direction ="left"    



win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)