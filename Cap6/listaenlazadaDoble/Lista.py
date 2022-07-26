

from NodoDoble import NodoDoble
import graphviz as graphviz

class ListaEnlazadaDoble:

    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def insertar(self,dato):
        if self.tamaño == 0:
            self.primero = dato
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = dato
            aux.siguiente.anterior = aux
        self.tamaño += 1

    def eliminar(self,dato):
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            if self.primero.dato == dato:
                self.primero = self.primero.siguiente
                self.primero.anterior = None
                self.tamaño -= 1
            else:
                aux = self.primero
                while aux.siguiente != None:
                    if aux.siguiente.dato == dato:
                        aux.siguiente = aux.siguiente.siguiente
                        if(aux.siguiente != None):
                            aux.siguiente.anterior = aux
                        self.tamaño -= 1
                        return
                    aux = aux.siguiente
                print("No se encontro el dato")
                

    def buscar(self,dato):
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux != None:
                if aux.dato == dato:
                    return aux
                aux = aux.siguiente
            print("No se encontro el dato")
        return None

    def getDatos(self):
        salidaDerecha = ''
        salidaInversa = ''
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux.siguiente != None:
                salidaDerecha += str(aux.dato) + ' -> '
                aux = aux.siguiente
            salidaDerecha += str(aux.dato)+' -> None'

            while aux.anterior != None:
                salidaInversa =  ' <- '+ aux.dato + salidaInversa
                aux = aux.anterior
            salidaInversa = 'None <- ' + aux.dato + salidaInversa

            print("---------- salida derecha ----------")
            print(salidaDerecha)
            print("---------- salida inversa ----------")
            print(salidaInversa)

    def graficar(self):
        nodesCount = 1
        dot = graphviz.Digraph(comment='Lista enlazada simple')
        aux = self.primero
        while aux != None:
            dot.node('n'+str(nodesCount),str(aux.dato))
            nodesCount += 1
            aux = aux.siguiente
        nodesCount -= 1
        while nodesCount > 1:
            dot.edge('n'+str(nodesCount-1),'n'+str(nodesCount), constraint='false')
            dot.edge('n'+str(nodesCount),'n'+str(nodesCount-1), constraint='false')
            nodesCount -= 1
        print(dot.source)
        dot.render('doctest-output/lista.gv', view=True) 
        'doctest-output/lista.gv.pdf'


lista = ListaEnlazadaDoble()
lista.getDatos()
print("################## insertar ##################")
lista.insertar(NodoDoble("Juan")) # 1
lista.insertar(NodoDoble("Pedro"))  # 2
lista.insertar(NodoDoble("Maria")) # 3
lista.insertar(NodoDoble("Cesar")) # 4


lista.getDatos()
#lista.graficar()

print("################## eliminar ##################")
lista.eliminar("Pedro")
lista.getDatos()
#lista.graficar()