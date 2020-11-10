import turtle
#from turtle import *
from random import randrange
from freegames import square,vector
print(2)
t = turtle.Screen()
food = vector(0,0)
snake = [vector(10,0)]
aim = vector(0,-10)

def change(x,y):
    aim.x = x
    aim.y = y
def inside(head):
    return -200<head.x<190 and -200<head.y<190
def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x,head.y,9,'red')
        turtle.update()
        return
    snake.append()
    if head==food:
        print("snake",len(snake))
        food.x = randrange(-15,15)*10
        food.y = randrange(-15,15)*10
    else:
        snake.pop()
    turtle.clear()

    for body in snake:
        square(body.x,body.y,9,'green')

    square(food.x,food.y,9,'red')
    turtle.update()
    turtle.ontimer(move,100)

    turtle.hideturtle()
    turtle.tracer(False)
    turtle.listen()
    turtle.onkey(lambda:changes(10,0),'Right')
    turtle.onkey(lambda:changes(10,0),'Left')
    turtle.onkey(lambda:changes(10,0),'Up')
    turtle.onkey(lambda:changes(10,0),'Down')

    move()
    turtle.done()
