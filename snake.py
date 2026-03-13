from browser import document, timer
from collections import deque
import random

canvas = document["game"]
ctx = canvas.getContext("2d")

cell = 20
rows = 30
cols = 30

snake = deque([(15,15),(15,14),(15,13)])
snake_set = set(snake)

direction = (0,1)

food = (10,10)

score = 0
speed = 120

paused = False
game_over = False


def spawn_food():
    while True:
        pos = (
            random.randint(0, rows-1),
            random.randint(0, cols-1)
        )
        if pos not in snake_set:
            return pos


def draw():

    ctx.fillStyle = "black"
    ctx.fillRect(0,0,600,600)

    ctx.strokeStyle = "#333"

    # grid
    for i in range(rows):
        ctx.beginPath()
        ctx.moveTo(0,i*cell)
        ctx.lineTo(cols*cell,i*cell)
        ctx.stroke()

    for j in range(cols):
        ctx.beginPath()
        ctx.moveTo(j*cell,0)
        ctx.lineTo(j*cell,rows*cell)
        ctx.stroke()

    # snake
    for i,(x,y) in enumerate(snake):

        if i == 0:
            ctx.fillStyle = "yellow"
        else:
            ctx.fillStyle = "lime"

        ctx.fillRect(y*cell,x*cell,cell,cell)

    # food
    fx,fy = food
    ctx.fillStyle="red"
    ctx.fillRect(fy*cell,fx*cell,cell,cell)


def move():

    global food, score, speed, game_over

    head = snake[0]

    dx,dy = direction
    new_head = (head[0] + dx, head[1] + dy)

    # wall collision
    if new_head[0] < 0 or new_head[0] >= rows or new_head[1] < 0 or new_head[1] >= cols:
        game_over = True
        return

    # self collision
    if new_head in snake_set:
        game_over = True
        return

    if new_head == food:

        snake.appendleft(new_head)
        snake_set.add(new_head)

        score += 1

        if score % 5 == 0:
            speed = max(40, speed - 10)

        document["score"].text = f"Score: {score} | Speed: {speed}"

        food = spawn_food()

    else:

        snake.appendleft(new_head)
        snake_set.add(new_head)

        tail = snake.pop()
        snake_set.remove(tail)


def change_direction(e):

    global direction, paused

    key = e.key

    if key == "p" or key == "P":
        paused = not paused
        return

    if key == "ArrowUp" and direction != (1,0):
        direction = (-1,0)

    elif key == "ArrowDown" and direction != (-1,0):
        direction = (1,0)

    elif key == "ArrowLeft" and direction != (0,1):
        direction = (0,-1)

    elif key == "ArrowRight" and direction != (0,-1):
        direction = (0,1)


def restart(e):

    global snake, snake_set, direction, food, score, speed, game_over

    snake = deque([(15,15),(15,14),(15,13)])
    snake_set = set(snake)

    direction = (0,1)

    food = spawn_food()

    score = 0
    speed = 120

    game_over = False

    document["score"].text = "Score: 0 | Speed: 120"

    game_loop()


def game_loop():

    if game_over:

        ctx.fillStyle="white"
        ctx.font="40px Arial"
        ctx.fillText("GAME OVER",190,300)
        return

    if paused:

        ctx.fillStyle="yellow"
        ctx.font="40px Arial"
        ctx.fillText("PAUSED",240,300)

        timer.set_timeout(game_loop,speed)
        return

    move()
    draw()

    timer.set_timeout(game_loop,speed)


document.bind("keydown",change_direction)
document["restart"].bind("click",restart)

food = spawn_food()

game_loop()