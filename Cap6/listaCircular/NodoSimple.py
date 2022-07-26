
class NodoSimple:

    def __init__(self,dato) -> None:
        self.siguiente:NodoSimple = None
        self.anterior:NodoSimple = None
        self.dato = dato

    def getDato(self):
        return self.dato

    def setDato(self, dato) -> None:
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, siguiente) -> None:
        self.siguiente = siguiente

    def getAnterior(self):
        return self.anterior

    def setAnterior(self, anterior) -> None:
        self.anterior = anterior