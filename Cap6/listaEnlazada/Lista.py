

from NodoSimple import NodoSimple
import graphviz

class ListaEnlazadaSimple:

    def __init__(self):
        self.primero:NodoSimple = None
        self.tamaño = 0

    def insertar(self,dato):
        if self.tamaño == 0:
            self.primero = dato
        else:
            aux:NodoSimple = self.primero
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(dato)
        self.tamaño += 1

    def eliminar(self,dato):
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            aux = self.primero
            if(aux.getDato() == dato):
                self.primero = aux.getSiguiente()
                self.tamaño -= 1
            else:
                while aux.getSiguiente() != None:
                    if aux.getSiguiente().dato == dato:
                        aux.setSiguiente(aux.getSiguiente().getSiguiente())
                        self.tamaño -= 1
                        break
                    aux = aux.getSiguiente()
                if aux.getSiguiente() == None:
                    print("No se encontro el dato")

    def buscar(self,dato):
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux != None:
                if aux.getDato() == dato:
                    return aux
                aux = aux.getSiguiente()
            print("No se encontro el dato")
        return None

    def getDatos(self):
        salida = ''
        if self.tamaño == 0:
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux != None:
                salida += str(aux.dato) + ' -> '
                aux = aux.getSiguiente()
            salida += 'None'
            print(salida)

    def graficar(self):
        nodesCount = 1
        dot = graphviz.Digraph(comment='Lista enlazada simple')
        aux = self.primero
        while aux != None:
            dot.node('n'+str(nodesCount),str(aux.dato))
            nodesCount += 1
            aux = aux.getSiguiente()
        nodesCount -= 1
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