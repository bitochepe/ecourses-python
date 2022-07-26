#------------------------------- Indentacion ---------------------------------
#Ejemplo 1: Indentado con tabulacion
from re import T


def Saludar():
    print("Hola Mundo")

def ImprimirMasGrande(x,y):
    if x > y:
        print(x)
    else:
        print(y)

#Ejemplo 2: indentado con 1 espacio
def Saludar():
 print("Hola Mundo")

def ImprimirMasGrande(x,y):
 if x > y:
  print(x)
 else:
  print(y)

#------------------------------- Comentarios ---------------------------------
#Este comentario es para que el editor de texto lo ignore
#Los comentarios de una sola linea se escriben con 
#Los comentarios de varias lineas se escriben con 
#Se pueden poner comentarios en varias lineas

"""Este comentario es para que el editor de texto lo ignore
Los comentarios de una sola linea se escriben con 
Los comentarios de varias lineas se escriben con 
Se pueden poner comentarios en varias lineas"""


def Saludar(nombre):
    print("Hola", nombre)

#Los comentarios no se ejecutan
Saludar("Juan") #Todo lo que esta despues de # es ignorado

'''
Los comentarios de varias lineas se pueden poner
con triple comillas dobles o simples
'''


#------------------------------- Tipos de datos ---------------------------------
#integers
print(10, 5402, 213079513205971235079)

#bases distintas
print(0B10, 0O10, 0X10)

#floats
print(12.64, 112139851239085.550123509218356, 2. , .33, 1.25e2, 1.25e-2)
print(1.8e308, 1.79e308, 5e-324, 1e-324)
print(18+4j, 1+3j)

#Strings
print("Hola", "Mundo", "!")
print('Hola' + 'Mundo' + '!') 

print("Texto que contiene comillas dobles: "Hola Mundo"") #esta linea contiene un error del mal uso de comillas
print("Texto que contiene comillas simples: 'Hola'")
print('Texto que contiene comillas dobles: "Hola"')
print("Texto delimitado con comillas dobles: \" usando backslash: \\")
print("Texto con salto de linea\
 ignorado")

print(r"No se utiliza el escape \"")
print(""" 
============================
     "Ejemplo de texto"
============================
""")

print(True, False)
if 0:
    print("Si")
else:
    print("No")

print(ord('C'))
print(chr(67))

#------------------------------- Variables ---------------------------------
var = "Hola" #Variable de tipo string
MiVariable = 100 #Variable de tipo entero
var_bool = True #Variable de tipo booleano
var10 = 45.10 #Variable de tipo float

x = y = z = 10 #Variables de tipo entero

#pruebas del manejo de variables
var2 = var
print(var)
print(var2)

#se reasigna el valor de la variable print que por defecto tiene el metodo naivo print asociado
var = 20
print(var) #20
print = 10
print(var) #error

#------------------------------- Sentencias ---------------------------------
x = 10
if x > 5: 
    print("Si")

x = 10
if x < 5:
    print("Si")
else:
    print("No")

x = "python"
if x == "sentencia":
    print("Aqui no entra")
elif x == "hola":
    print("Aqui no entra")
elif x == "python":
    print("Aqui entra")
else:
    print("Aqui no entra")

x = "python"
if x == "python": print("Aqui entra")
if x == "python": print("Esta sentencia"); print("Esta otra"); print("se ejecutan")
if x == "Sentencia": print("Aqui"); print("No entra")
elif x == "hola": print("Aqui"); print("No entra")
elif x == "python": print("Aqui"); print("entra")
else: print("Aqui"); print("No entra")

x = 10
print("x es igual a 10") if x == 10 else print("x es diferente a 10")

#------------------------------- for ---------------------------------
x = [1,2,3,4,5]
for i in x:
    print(i)

x= ["valor1","valor2","valor3"]
iterador = iter(x)
next(iterador)
next(iterador)
next(iterador)

#------------------------------- while ---------------------------------
x = 5
while x > 0:
    print(x)
    x -= 1

x= ["valor1","valor2","valor3"]
while x:
    print(x.pop(-1))


#------------------------------- break, continue, else, pass ---------------------------------
while True:
    print("while \"infinito\"")
    break

for x in (1,2,3,4,5,6,7,8,9,10,11,12):
    if x%2 == 0:
        print(x)

for x in (1,2,3,4,5):
    if x%2 != 0:
        print(x)
else:
    print("si")

for x in (1,2,3,4,5):
    if x>3:
        break
    else:
        print(x)
else:
    print("si")

for x in (1,2,3):
    #no hay cuerpo
    pass
print("for ejecutado")