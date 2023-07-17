from modCarrera import Carrera

class Facultad:
    
    
    def __init__(self, cod, nbre, dir, local, tel) -> None:
        
        self.__cod = cod
        self.__nbre = nbre
        self.__dir = dir
        self.__local = local
        self.__tel = tel
        self.__carreras :list[Carrera] = []

    def getCod(self):
        
        return self.__cod
    
    def getNbre(self):
        
        return self.__nbre
    
    def getLocal(self):
        
        return self.__local
    
    def setCarreras(self,carrera):
        
        self.__carreras.append(carrera)
    
    def getCarreras(self) -> list[Carrera]:
        
        return self.__carreras

    def __repr__(self):
        
        return f"{self.__cod} - {self.__nbre} - {self.__dir} - {self.__local} - {self.__tel} - {self.__carreras}"
