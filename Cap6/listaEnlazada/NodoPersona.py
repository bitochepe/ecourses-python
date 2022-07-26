from Persona import Persona

class NodoPersona:

    def __init__(self,persona) -> None:
        self.siguiente:NodoPersona = None
        self.anterior:NodoPersona = None
        self.dato:Persona = persona

    def __getDato__(self) -> Persona:
        return self.dato

    def __setDato__(self, persona: Persona) -> None:
        self.dato = persona

    def __getSiguiente__(self):
        return self.siguiente
    
    def __setSiguiente__(self, siguiente) -> None:
        self.siguiente = siguiente

    def __getAnterior__(self):
        return self.anterior

    def __setAnterior__(self, anterior) -> None:
        self.anterior = anterior