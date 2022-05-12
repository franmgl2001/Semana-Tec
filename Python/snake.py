"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

"Counters"
food = vector(0, 0) #Exercise 3. Helps the food move
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    #Exercise 4. If you change the values of x and y it will respond different
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    #Exercise 2. Lets you move boundaries and lets the snake move around the edges
    "Return True if head inside boundaries."
    return -220 < head.x < 200 and -210 < head.y < 200

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    "Works to change score along the food"
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    "Changes size of snake based on the food"
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    "Changes the color and size of snake"
    for body in snake:
        square(body.x, body.y, 9, 'blue')

    "Changes the color and size of food"
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 90) #Exercise 1. Makes the snake move faster or slower by moving the time

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#Exercise 4. When you press the arrows the snake
#moves 10 pixels and if you change the values it will be more.
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
