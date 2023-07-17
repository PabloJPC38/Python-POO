from modInscripcion import Incripcion
from ctrTaller import ManejadorTaller
from datetime import datetime
from modPersona import Persona

class ManejadorInscripcion:
    
    def __init__(self) -> None:
        
        self.__inscripciones : list[Incripcion] = []
    
    def getInscripciones(self):
        
        return self.__inscripciones
    
    """def incripcion(self, talleres : ManejadorTaller):
        
        respuesta = input("Desea inscribirse a un taller? (s/n) :")
        band = True
        i = 0
        
        while band:
            
            if respuesta == "s":
                
                talleres.getTaller()
                
                i = int(input("Ingrese taller:"))
                
                if talleres.vacanteTaller(i - 1):
            
                    print(f"Hay vacantes!!")
                    
                    persona = Persona(input("Ingrese nombre de la persona:"),input("Ingrese dirección:"),input("Ingrese DNI:"))
                    inscripcion = Incripcion(datetime.now().date(),False,persona,talleres.getTalleres()[i])
                    
                    print(f"Incripto al taller '{talleres.getTalleres()[i].getNbre()}'!!")
                    
                    self.__inscripciones.append(inscripcion)
                    
                else:
            
                    print(f"No hay más vacantes para el taller '{talleres.getTalleres()[i].getNbre()}'!!)")
            
            elif respuesta == "n":
                
                band = False
            
            respuesta = input("Desea inscribirse a un taller? (s/n) :")
    
    def consultarInscripcion(self, dni):
        
        band, i = True, 0
        
        while(band and i < len(self.__inscripciones)):
            
            if self.__inscripciones[i].getPersona().getDNI() == dni:
                
                print(f"Taller:{self.__inscripciones[i].getTaller().getNbre()} - Monto:{self.__inscripciones[i].getTaller().getMonto()}")
                band = False
        
        if band and i == len(self.__inscripciones):
            
            print("No se encuentra inscripta esa persona en ningún taller")
    
    """
