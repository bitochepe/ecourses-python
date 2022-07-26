class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.apellido, self.edad)
    
    def __setNombre__(self, __nombre: str) -> None:
        self.nombre = __nombre

    def __getNombre__(self) -> str:
        return self.nombre

    def __setApellido__(self, __apellido: str) -> None:
        self.apellido = __apellido

    def __getApellido__(self) -> str:
        return self.apellido

    def __setEdad__(self, __edad: int) -> None:
        self.edad = __edad

    def __getEdad__(self) -> int:
        return self.edad