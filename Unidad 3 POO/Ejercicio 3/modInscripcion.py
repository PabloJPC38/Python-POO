from modPersona import Persona
from modTaller import Taller


class Incripcion:
    
    def __init__(self, fecha, pago, person, taller) -> None:
        
        self.__fecha = fecha
        self.__pago = pago
        self.__person : Persona = person
        self.__taller : Taller = taller
    
    def getFecha(self):
        
        return self.__fecha
    
    def setPago(self, pago):
        
        self.__pago = pago
    
    def getPago(self):
        
        return self.__pago
    
    def getPersona(self):
        
        return self.__person
    
    def getTaller(self):
        
        return self.__taller