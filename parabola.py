'''Data la parabola X**2 + bx + c, definire delle funzioni che ne calcolino il vertice e il fuoco utilizzando i coefficienti a, b e c inseriti
dall'utente'''

a = float(input("Inserire a "))
b = float(input("Inserire b "))
c = float(input("Inserire c "))


def delta(a, b, c):
    D = b**2 - 4*a*c
    return D

def vertice(a, b, c):
    D = delta(a, b, c)
    Xv = float(-b/(2*a))
    Yv = float(-D/(4*a))
    return Xv and Yv

def fuoco(a, b, c):
    D = delta(a, b, c)
    Xf = float(-b/(2*a))
    Yf = float((1-D)/(4*a))
    return Xf and Yf

'''
print(vertice(a, b, c))
print(fuoco(a, b, c))
'''
