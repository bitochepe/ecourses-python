

from NodoSimple import NodoSimple
import graphviz

class ListaEnlazadaSimple:

    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def insertar(self,dato):
        if self.tamaño == 0:
            self.primero = dato
            dato.siguiente = self.primero
        else:
            aux = self.primero
            while aux.siguiente != self.primero:
                aux = aux.siguiente
            aux.siguiente = dato
            dato.siguiente = self.primero
        self.tamaño += 1

    def eliminar(self,dato):
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux.siguiente != self.primero:
                if aux.siguiente.dato == dato:
                    aux.siguiente = aux.siguiente.siguiente
                    self.tamaño -= 1
                    break
                aux = aux.siguiente
            if aux.siguiente == self.primero:
                if aux.siguiente.dato == dato:
                    self.primero = aux.siguiente.siguiente
                    aux.siguiente = self.primero
                    self.tamaño -= 1
                else:
                    print("No se encontro el dato")

    def buscar(self,dato):
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux.siguiente != self.primero:
                if aux.dato == dato:
                    return aux
                aux = aux.siguiente
            print("No se encontro el dato")
        return None

    def getDatos(self):
        salida = ''
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux.siguiente != self.primero:
                salida += str(aux.dato) + ' -> '
                aux = aux.siguiente
            salida += str(aux.dato) + ' -> ' + str(self.primero.dato)
            print(salida)

    def graficar(self):
        nodesCount = 1
        dot = graphviz.Digraph(comment='Lista circular simple')
        aux = self.primero
        while aux.siguiente != self.primero:
            dot.node('n'+str(nodesCount),str(aux.dato))
            nodesCount += 1
            aux = aux.siguiente
        dot.node('n'+str(nodesCount),str(aux.dato))
        dot.edge('n'+str(nodesCount),'n1', constraint='false')
        while nodesCount > 1:
            dot.edge('n'+str(nodesCount-1),'n'+str(nodesCount), constraint='false')
            nodesCount -= 1
        print(dot.source)
        dot.render('doctest-output/lista.gv', view=True)  # doctest: +SKIP
        'doctest-output/lista.gv.pdf'        

lista = ListaEnlazadaSimple()
lista.getDatos() #Se espera lista vacia

lista.insertar(NodoSimple("Juan"))
lista.insertar(NodoSimple("Pedro"))
lista.insertar(NodoSimple("Maria"))
lista.insertar(NodoSimple("Cesar"))

lista.getDatos() #Se espera Juan, Pedro, Maria, Cesar

print(lista.buscar("Juan").dato) #Se espera Juan

lista.eliminar("Maria")
lista.getDatos() #Se espera Juan, Pedro, Cesar

lista.insertar(NodoSimple("Luis"))
lista.getDatos() #Se espera Juan, Pedro, Cesar, Luis

lista.graficar()
