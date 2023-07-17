


class Taller:
    
    def __init__(self, id, nbre, vacante, monto) -> None:
        
        self.__id = int(id)
        self.__nbre = nbre
        self.__vacante = int(vacante)
        self.__monto = float(monto)
        self.__incrip = []
        
    
    def getId(self):
        
        return self.__id
    
    def getNbre(self):
        
        return self.__nbre
    
    def setVacante(self):
        
        self.__vacante -= 1
    
    def getVacante(self):
        
        return self.__vacante
    
    def getMonto(self):
        
        return self.__monto
    
    def getIncrip(self):
        
        return self.__incrip
    
    def setInscrp(self, inscripcion):
        
        self.__incrip.append(inscripcion)