import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off-screen updates

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []
brick_colors = ["red", "orange", "yellow", "green", "blue"]
brick_width = 70
brick_height = 20
brick_rows = 5
brick_cols = 8

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(brick_colors[row % len(brick_colors)])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        x = -290 + col * brick_width
        y = 200 - row * brick_height
        brick.goto(x, y)
        bricks.append(brick)

# Paddle movement
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision checking
    if ball.xcor() > 390:
        ball.dx *= -1
    elif ball.xcor() < -390:
        ball.dx *= -1
    elif ball.ycor() > 290:
        ball.dy *= -1

    # Paddle collision checking
    if (ball.ycor() < -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Brick collision checking
    for brick in bricks:
        if (brick.ycor() - brick_height/2 < ball.ycor() < brick.ycor() + brick_height/2) and \
                (brick.xcor() - brick_width/2 < ball.xcor() < brick.xcor() + brick_width/2):
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move the brick off-screen upon collision

