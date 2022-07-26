class Coche:
    """Esta clase define el estado y el comportamiento de un Coche"""

    ruedas = 4

    def __init__(self,color,aceleracion) -> None:
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self) -> None:
        self.velocidad += self.aceleracion

    def frenar(self) -> None:
        v = self.velocidad - self.aceleracion
        if v < 0:
            self.velocidad = 0
        else:
            self.velocidad = v


c1 = Coche("rojo",20)
print(c1.color)
print(c1.ruedas)
c2 = Coche("azul",30)
print(c2.color)
print(c2.ruedas)

print(c1.marchas) # Error porque no existe el atributo marchas

#------------------------Metodos----------------------------------------
c1 = Coche("rojo",20)
c2 = Coche("azul",30)
print(c1.color)
print(c2.color)
print(c1.ruedas) #atributo de la clase
print(c2.ruedas) #atributo de la clase
Coche.ruedas = 6 #atributo de la clase
print(c1.ruedas) #atributo de la clase
print(c2.ruedas) #atributo de la clase

c1.ruedas = 6 #atributo de la instancia
print(c1.ruedas) #atributo de la instancia
print(c2.ruedas) #atributo de la clase
print(Coche.ruedas) #atributo de la clase

#------------------------Herencia-------------------------------------
class CocheVolador(Coche):
    ruedas = 6

    def __init__(self,color,aceleracion,esta_volando=False) -> None:
        super().__init__(color,aceleracion)
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False


#----------------------Herencia multiple--------------------------------
class A:
    def print_a(self):
        print("A")
class B:
    def print_b(self):
        print("B")
class C(A,B):
    def print_c(self):
        print("C")

c = C()
c.print_a()
c.print_b()
c.print_c()

#----------------------Encapsulamiento--------------------------------
class A:
    def __init__(self):
        self._contador = 0 #atributo privado
    def incrementa(self):
        self._contador += 1
    def cuenta(self):
        return self._contador

class B:
    def __init__(self):
        self.__contador = 0 #atributo privado
    def incrementa(self):
        self.__contador += 1
    def cuenta(self):
        return self.__contador

a = A()
a.incrementa()
a.incrementa()
a.incrementa()
print(a.cuenta())
print(a._contador)
b = B()
b.incrementa()
b.incrementa()
print(b.cuenta())
print(b._contador) #error porque esta privado


#----------------------Polimorfismo--------------------------------
class Perro:
    def sonido(self):
        print("Guauuuuuu!!!")

class Gato:
    def sonido(self):
        print("Miauuuuuu!!!")

class Vaca:
    def sonido(self):
        print("Muuuuuuuu!!!")

def a_cantar(animales):
    for animal in animales:
        animal.sonido()

perro = Perro()
gato = Gato()
gato_2 = Gato()
vaca = Vaca()
perro_2 = Perro()
granja = [perro,gato,vaca,perro_2,gato_2]
a_cantar(granja)

#---------------------Decoradores--------------------------------
def midecorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@midecorador
def suma(a, b):
    print("Entra en la funcion suma")
    return a + b
suma(5,8)

#-----------------Decoradores con parametros----------------------------
def mi_decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@mi_decorador("Imprime esto antes y despues")
def suma(a, b):
    print("Entra en la funcion suma")
    return a + b


