import turtle, random, math

screen = turtle.Screen()
screen.bgcolor("black")
screen.delay(0)
screen.register_shape('paddle',((-30,-10), (-30,10), (30,10), (30,-10)))

sprite = turtle.Turtle()
sprite.penup()
sprite.speed(0)
sprite.color("white")
sprite.ht()

paddle1 = sprite.clone()
paddle1.shape("paddle")
paddle1.st()
paddle2 = paddle1.clone()
paddle1.goto(160, 0)
paddle2.goto(-160, 0)

puck = sprite.clone()
puck.shape("circle")
puck.goto(0,0)
puck.seth(0)
puck.st()

speed = 5
edge = 200
dx = random.uniform(0.5,1)*speed
dy = ((speed**2)-(dx**2))**0.5

def update():
    global dx, dy
    x = puck.xcor()
    y = puck.ycor()
    if(math.fabs(x) > edge):
        dx = -dx
    elif(math.fabs(y) > edge):
        dy = -dy

    puck.goto(x+dx,y+dy)
    screen.ontimer(update, 10)

update()

def check_collided(paddle):
    if(math.fabs(paddle.xcor() - puck.xcor()) < 15 and math.fabs(paddle.ycor() - puck.ycor()) < 35):
        return True

    return False

def update():
    global dx, dy
    x = puck.xcor()
    y = puck.ycor()
    if(math.fabs(x) > edge or check_collided(paddle1) or check_collided(paddle2)):
        dx = -dx
    elif(math.fabs(y) > edge):
        dy = -dy

    puck.goto(x+dx,y+dy)
    screen.ontimer(update, 10)

def right_up():
    if(edge-paddle1.ycor() > 30):
        paddle1.goto(paddle1.xcor(), paddle1.ycor()+20)

def right_down():
    if(edge+paddle1.ycor() > 30):
        paddle1.goto(paddle1.xcor(), paddle1.ycor()-20)

def left_up():
    if(edge-paddle2.ycor() > 30):
        paddle2.goto(paddle2.xcor(), paddle2.ycor()+20)

def left_down():
    if(edge+paddle2.ycor() > 30):
        paddle2.goto(paddle2.xcor(), paddle2.ycor()-20)

screen.onkey(right_up, "Up")
screen.onkey(right_down, "Down")
screen.onkey(left_up, "W")
screen.onkey(left_down, "S")
screen.listen()