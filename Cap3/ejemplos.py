#-----------------------------Listas----------------------------------
lista = [12, "Hola", True, [1,2,3], 34.10]
lista[1] = "Adios"

#------------------------------Tuplas---------------------------------
tupla1 = (1, 10.25, -24.32, "Guatemala")
tupla2 = (2, 45.20, -123.90, "Peten")
print(tupla1)

print(tupla1[0])
tupla1[0] = "Nuevo valor"

#-------------------Empquetado y desempaquetado-----------------------
x = 100
y = 200
z = "300"

tupla3 = x, y, z
print(tupla3)

a,b,c,d = tupla1
print(a); print(b); print(c); print(d)

#-----------------------------Pilas-----------------------------------
pila = [1, 2, 3, 4, 5] #una lista de numeros pero sera manejada como una pila
pila.append(6) #agrega un elemento al final de la lista o al top de la pila
print(pila)

x = pila.pop() #elimina el ultimo elemento
print(x) #muestra el elemento eliminado

print(pila) #muestra la pila ya sin el elemento

#------------------------------Colas-----------------------------------
cola = [1, 2, 3, 4, 5] #una lista de numeros pero sera manejada como una cola
cola.append(6) #agrega un elemento al final de la lista o al bottom de la cola
print(cola)

x = cola.pop(0) #elimina el primer elemento de la cola
print(x) #muestra el elemento eliminado

print(cola) #muestra la cola ya sin el elemento

#---------------------------------------------------------------------
thisdict = {
	"brand": "Ford",
	"electric": False,
	"year": 1964,
	"colors": ["red", "white", "blue"]
}
print(thisdict)