#--------------------------Funciones-----------------------------
#Funcion que imprime la cadena "Hola"
import re
from sys import api_version


def miFuncion():
    print("Hola")

#Funcion que recibe 2 numeros como parametros
#e imprime la suma de ellos
def suma(num1, num2):
    print(num1+num2)

#Funcion que recibe 2 numeros como parametros
#y retorna al mayor
def mayor(num1, num2):
    if num1 > num2:
        return num1
    return num2

def saludar(nombre):
    return "Hola "+ nombre
saludar("Juan")

#------------------------Retorno Multiple----------------------
def retornoMultiple():
    return 1,2,3,4,5
print(retornoMultiple())

a, b, c, d, e = retornoMultiple()
print(a); print(b); print(c); print(d); print(e)


#--------------------------Parametros--------------------------
def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')
 
f(6, 'banana') # error: missing argument 'price'
f(6, 'banana', 1.74, 'kumquats')

f(qty=6, item='banana', price=1.74)
f(qty=6, item='banana', cost=1.74) #error porque no se puede llamar cost

f(item='banana', qty=6, price=1.74)
f(6, price=1.74, item='banana')
f(6, 'banana', price=1.74)
f(6, price=1.74,'banana') #error parametro posicional

def f(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')
f(4,'apples')

def f(fx):
    fx = 10
x=5
f(x)
x

f(4, 'apples')
my_dict = {'foo': 1,'bar':2, 'baz': 3}
f(my_dict)
my_dict

#-------------------------Docstrings-------------------------
def avg(*args):
    """Return the average of a list of numeric values"""
    return sum(args) / len(args)

#------------------------Anotaciones-------------------------
f.__annotations__

#-----------------------Orden superior-----------------------
def higher_order_function(fun):
    fun()

def greating():
    print("Hello World")

higher_order_function(greating)

#---------------------------Labmda---------------------------
def even_numbers(nums):
    evenlist = []
    for n in nums:
        if n % 2 == 0:
            evenlist.append(n)
    return evenlist

num_list = [10, 5, 12, 78, 6, 1, 7, 9]
ans = even_numbers(num_list)
print("Even numbers are:", ans)

l = [10, 5, 12, 78, 6, 1, 7, 9]
even_nos = list(filter(lambda x: x % 2 == 0, l))
print("Even numbers are:", even_nos)