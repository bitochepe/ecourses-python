#-----------------------------lista de errores---------------------------
# descomentar para ver los errores
"""
while True print("Hello World") # error de sintaxis
10 * (1/0) # error de division por cero
4 + spam + 3 # error de variable no definida
'2' + 2 # error de tipo de dato
"""
#----------------------------Manejo de errores---------------------------
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


#----------------------Manipulacion de archivos---------------------------
fobj = open('PythonExamplefile.txt', 'r')
#operations on file
fobj.close()

fobj = open('PythonExamplefile.txt', 'r')
print("File name: ", fobj.name)
print("File mode: ", fobj.mode)
fobj.close()

#----------------------Escribir en archivos---------------------------
fobj = open('PythonExamplefile.txt', 'w')
fobj.write("Hello Python programming")
fobj.close()

#----------------------Leer archivos---------------------------
archivo = open('archivo.txt', 'r')
cadena1 = fobj.read(9)
cadena2 = fobj.read()
print(cadena1)
print(cadena2)
archivo.close()

archivo = open('archivo.txt', 'r')
#Lee todas las lineas y asigna a una lista
lista = archivo.readlines()
numlin = 0
#Recorre todas los elementos de la lista
for linea in lista:
    print(numlin, linea)
    numlin += 1
archivo.close()

#----------------------Renombrar y eliminar archivos---------------------------
import os
os.rename('PythonExamplefile.txt', 'Python.txt.txt') #Renombra el archivo
os.remove('Python.txt.txt') #Elimina el archivo

