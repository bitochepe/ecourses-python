
class NodoSimple:

    def __init__(self,dato) -> None:
        self.siguiente:NodoSimple =None
        self.dato = dato

    def getDato(self):
        return self.dato

    def setDato(self, dato) -> None:
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, siguiente) -> None:
        self.siguiente = siguiente

class Dato:

    def __init__(self,valor) -> None:
        self.valor = valor

    def getValor(self):
        return self.valor

    def setValor(self, valor) -> None:
        self.valor = valor