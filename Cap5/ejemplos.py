#----------------------Scopes---------------------------
def funcion_a():
    y = 2
    def funcion_b():
        z = 3
        print(z)
    funcion_b()
    print(y)
x = 1
funcion_a()
print(x)

def funcion_a():
    global x
    x = 2
    def funcion_b():
        global x
        x = 3
        print(x)
    funcion_b()
    print(x)
x = 1
funcion_a()
print(x)


#----------------------Modulos--------------------------
import aritmetica
print(aritmetica.sumar(1, 2))

from aritmetica import *

mult(10,10)
div(200,5)

from aritmetica import resta as rst
rst(4,2)
