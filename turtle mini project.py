import turtle

turtle.bgcolor('white')
turtle.pensize(2)
turtle.speed(0)

def cuadrado():
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)

def poligono(n):
    for i in range(n):
        turtle.forward(50)
        turtle.left(360 / n)

def dibujador():
    n = int(input('Cuantos lados quieres que tenga la figura: '))
    for i in range(6):
        for colors in ['red', 'blue', 'green', 'cyan', 'yellow', 'black']:
            turtle.color(colors)
            poligono(n)
            turtle.left(10)
            turtle.pensize(2)

dibujador()




