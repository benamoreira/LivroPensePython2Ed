import turtle
import math
bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        print(square)

def polygon(t,n, length):
    angle = 360/n
    polyline(t, n, length, angle)
    print(polygon)

def circle(t, r):
    arc(t, r, 360)
    print(circle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)
    print(arc)

def polyline(t, n, length, angle):
    """Desenha n segmentos de reta com o comprimento dado e
    ânulo (em graus) entre eles. e é um turtle
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    print(polyline)


#square(bob, 100)
#polygon(bob, 7, 80)
circle(bob, 100)