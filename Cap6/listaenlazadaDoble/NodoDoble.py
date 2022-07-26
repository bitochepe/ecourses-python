
class NodoDoble:

    def __init__(self,dato) -> None:
        self.siguiente:NodoDoble = None
        self.anterior:NodoDoble = None
        self.dato = dato

    def __getDato__(self):
        return self.dato

    def __setDato__(self, dato) -> None:
        self.dato = dato

    def __getSiguiente__(self):
        return self.siguiente
    
    def __setSiguiente__(self, siguiente) -> None:
        self.siguiente = siguiente

    def __getAnterior__(self):
        return self.anterior

    def __setAnterior__(self, anterior) -> None:
        self.anterior = anterior