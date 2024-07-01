import turtle  # turtle is a library
import random  # here random use for food
import time

# create memory
delay = 0.1  # increase speed of snake(delay ko km krega)
sc = 0  # initial score in score card is 0.
hs = 0  # highest score card is 0 in starting
bodies = []

# create a screen
s = turtle.Screen()  # screen turtle lib mai hai
s.title("Snake Game")
s.bgcolor("light blue")  # all color not support light.
s.setup(width=600, height=600)  # size of screen.

# creating a head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")  # all head blue.
head.fillcolor("red")  # under the head red and border is blue.
head.penup()  # move kre to rigide line clean kre.
head.goto(0, 0)  # initial axis (x&y)
head.direction = "Stop"

# creating food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.penup()
food.ht()  # ht--hide turtle--food direct open.
food.goto(150, 200)  # food location
food.st()  # for showing a turtle.

# creating a score board
sb = turtle.Turtle()  # sb is variable
sb.penup()
sb.ht()
sb.goto(-250, 250)  # location of score board.
sb.write("Score : 0      |  Highest score : 0")  # to print a score card on the screen for the first time.


# create function for moving in all direction
def moveUp():
    if head.direction != "down":
        head.direction = "up"


def moveDown():
    if head.direction != "up":
        head.direction = "down"


def moveLeft():
    if head.direction != "right":
        head.direction = "left"


def moveRight():
    if head.direction != "left":
        head.direction = "right"


def moveStop():
    head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
# event handling (movement of snake)
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# main loop
while True:
    s.update()                            # to update the screen
    # check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.direction = "stop"
        # hide bodies
        for body in bodies:
            body.ht()
        bodies.clear()
        sc = 0
        delay = 0.1
        sb.clear()
        sb.write("Score: {}     |   Highest Score:{}".format(sc, hs))

    # check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)  # random lib has randint--means generate integr between -290 to 290 --- for re show the food--
        y = random.randint(-290, 290)
        food.goto(x, y)  # food move

        # increase the body of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)  # append the new body in list ----body ki size increase hoga

        sc = sc + 10  # increase the score
        delay = delay - 0.001  # increase the speed

        if sc > hs:
            hs = sc  # update highest score
        sb.clear()  # new score hoga to old wala clear
        sb.write("Score: {}    |  Highest Score: {}".format(sc, hs))

    # move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()

    # check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)  # Game over
            head.direction = "stop"
            # hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: {}     |   Highest Score: {}".format(sc, hs))
            break

    time.sleep(delay)

s.mainloop()
