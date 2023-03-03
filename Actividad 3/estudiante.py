'''Módulo que contiene la clase Estudiante.'''

class Estudiante:
    '''
    Ejemplos:
    >>> est1 = Estudiante("18989896S", 49, 8.5)
    >>> est2 = Estudiante("18978053V", 52, 7)
    >>> est1.mostrar_datos_estudiante()
    DNI: 18989896S
    Edad: 49
    Nota media: 8.5
    >>> est2.cambiar_nota_media(10) 
    >>> est2.mostrar_datos_estudiante()
    DNI: 18978053V
    Edad: 52
    Nota media: 10
    '''

    DNI: str
    '''El DNI del estudiante.'''
    edad: int
    '''La edad del estudiante.'''
    nota_media: float
    '''La nota media sacada por el estudiante.'''

    def __init__(self,DNI: str,edad: int,nota_media: float):
        '''Crea una instancia de la clase Estudiante.'''
        self.DNI = DNI 
        self.edad = edad
        self.nota_media = nota_media

    def mostrar_datos_estudiante(self):
        '''Método para mostrar los atributos de un estudiante.'''
        print("DNI:", self.DNI)
        print("Edad:", self.edad)
        print("Nota media:", self.nota_media)

    def cambiar_nota_media(self, nueva_nota):
        '''Método para cambiar la nota media de un estudiante.'''
        self.nota_media = nueva_nota