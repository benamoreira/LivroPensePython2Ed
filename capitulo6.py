import math

#COMPARE
x = 6
y = 4
z = 8

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

print("O Resultado da comparação é: ", compare(x,y))

# PITAGORAS
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

print("A Distancia é: ", distance(1,2,4,6))

print("\n")
# HIPOTENUSA
ca = float(input("Digite o cumprimento do Cateto Oposto: "))
co = float(input("Digite o cumprimento do Cateto Adjacente: "))

def hypotenuse(ca, co):
    return (co**2 + ca**2)**(1/2)

print("A hipotenusa é: {}".format(hypotenuse(ca, co)))

#CIRCULO
def area(radius):
    a = math.pi * radius**2
    return a

def circle_area(xc,yc, xp,yp):
    radius = distance(xc, yc,xp,yp)
    result = area(radius)
    return result

print("A Area do circulo é: {}".format(circle_area(1,2,4,6)))

#BOOLENAS
def is_divisible(x,y):
    return x % y == 0

print(is_divisible(6, 4))
print(is_divisible(6, 3))

if is_divisible(x, y):
    print('{} é divisivel por {}'.format(x, y))

def is_between(x,y,z):
    if x <= y <= z:
        return True
    else:
        return False

#FATORIAL
n = int(input('DIgite um numero Inteiro: '))
def factorial(n):
    if not isinstance(n, int):
        print('Fatorial é apenas definido por inteiros.')
        return None
    elif n < 0:
        print('FAtorial não poder ser definido com valores negativos.')
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("O Total de {}! (Fatorial) é: {}".format(n, factorial(n)))

#FIBONACCI
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("A sequencia Fibonacci de {} é: {}".format(n, fibonacci(n)))